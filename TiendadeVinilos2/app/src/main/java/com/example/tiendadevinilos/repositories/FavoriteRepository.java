package com.example.tiendadevinilos.repositories;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class FavoriteRepository {
    private final DatabaseReference favRef;
    private final String userId;

    public FavoriteRepository() {
        if (FirebaseAuth.getInstance().getCurrentUser() != null) {
            userId = FirebaseAuth.getInstance().getCurrentUser().getUid();
            favRef = FirebaseDatabase.getInstance().getReference("users").child(userId).child("favorites");
        } else {
            userId = null;
            favRef = null;
        }
    }

    public void addFavorite(String productId) {
        if (favRef != null && productId != null) {
            favRef.child(productId).setValue(true);
        }
    }

    public void removeFavorite(String productId) {
        if (favRef != null && productId != null) {
            favRef.child(productId).removeValue();
        }
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
}
