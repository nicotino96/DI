package com.example.tiendadevinilos.repositories;

import android.util.Log;

import com.example.tiendadevinilos.models.Product;
import com.google.android.gms.tasks.Task;
import com.google.android.gms.tasks.Tasks;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class FavoriteRepository {
    private final DatabaseReference favRef;
    private final DatabaseReference productsRef;
    private final String userId;

    public FavoriteRepository() {
        FirebaseUser currentUser = FirebaseAuth.getInstance().getCurrentUser();
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        if (currentUser != null) {
            userId = currentUser.getUid();
            favRef = FirebaseDatabase.getInstance().getReference("users").child(userId).child("favorites");
            productsRef = database.getReference("items");
            Log.d("FavoriteRepository", "Initialized with userId: " + userId);
        } else {
            userId = null;
            favRef = database.getReference();
            productsRef = database.getReference("items");
            Log.e("FavoriteRepository", "No user logged in!");
        }
    }

    public Task<Void> addFavorite(String productId) {
        if (favRef != null && productId != null) {
            return favRef.child(productId).setValue(true);
        }
        return Tasks.forException(new Exception("Invalid reference or product ID"));
    }

    public Task<Void> removeFavorite(String productId) {
        if (favRef != null && productId != null) {
            return favRef.child(productId).removeValue();
        }
        return Tasks.forException(new Exception("Invalid reference or product ID"));
    }


    public void checkIfFavorite(String productId, OnFavoriteCheckedListener listener) {
        if (favRef != null && productId != null) {
            favRef.child(productId).get().addOnSuccessListener(snapshot -> listener.onChecked(snapshot.exists()));
        } else {
            listener.onChecked(false);
        }
    }

    public interface OnFavoriteCheckedListener {
        void onChecked(boolean isFavorite);
    }
    public void getFavoriteItems(OnFavoriteItemsLoadedListener listener) {
        if (favRef == null) {
            listener.onLoaded(new ArrayList<>());
            return;
        }

        favRef.get().addOnSuccessListener(snapshot -> {
            List<Product> items = new ArrayList<>();
            int totalFavorites = (int) snapshot.getChildrenCount();
            AtomicInteger loadedCount = new AtomicInteger(0);

            if (!snapshot.hasChildren()) {
                listener.onLoaded(items);
                return;
            }

            for (DataSnapshot favoriteSnapshot : snapshot.getChildren()) {
                String productId = favoriteSnapshot.getKey();
                productsRef.child(productId).get().addOnSuccessListener(productSnapshot -> {
                    Product product = productSnapshot.getValue(Product.class);
                    if (product != null) {
                        items.add(product);
                    }

                    if (loadedCount.incrementAndGet() == totalFavorites) {
                        listener.onLoaded(items);
                    }
                }).addOnFailureListener(e -> {
                    if (loadedCount.incrementAndGet() == totalFavorites) {
                        listener.onLoaded(items);
                    }
                });
            }
        }).addOnFailureListener(e -> listener.onLoaded(new ArrayList<>()));
    }
    public interface OnFavoriteItemsLoadedListener {
        void onLoaded(List<Product> items);
    }
}
