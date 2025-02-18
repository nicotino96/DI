package com.example.tiendadevinilos.repositories;

import android.content.Context;
import android.content.SharedPreferences;
import androidx.appcompat.app.AppCompatDelegate;

import com.example.tiendadevinilos.models.Product;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;
import java.util.List;

public class ProfileRepository {
    private static final String PREFS_NAME = "AppPrefs";
    private static final String DARK_MODE_KEY = "dark_mode";

    private final FirebaseAuth auth;
    private final SharedPreferences sharedPreferences;
    private final DatabaseReference favRef;
    private final DatabaseReference productsRef;

    public ProfileRepository(Context context) {
        auth = FirebaseAuth.getInstance();
        sharedPreferences = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);

        FirebaseUser user = auth.getCurrentUser();
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        productsRef = database.getReference("items");

        // 🔹 Manejo seguro de favRef para evitar NullPointerException
        if (user != null) {
            favRef = database.getReference("users").child(user.getUid()).child("favorites");
        } else {
            favRef = null; // Evita errores si el usuario no está autenticado
        }
    }

    // 🔹 Cambiar contraseña del usuario autenticado
    public void changePassword(String newPassword, OnPasswordChangeListener listener) {
        FirebaseUser user = auth.getCurrentUser();
        if (user != null) {
            user.updatePassword(newPassword).addOnCompleteListener(task -> {
                if (task.isSuccessful()) {
                    listener.onSuccess();
                } else {
                    listener.onFailure(task.getException() != null ? task.getException().getMessage() : "Error desconocido");
                }
            });
        } else {
            listener.onFailure("No hay usuario autenticado.");
        }
    }

    public interface OnPasswordChangeListener {
        void onSuccess();
        void onFailure(String errorMessage);
    }

    // 🔹 Obtener el estado del modo oscuro
    public boolean isDarkModeEnabled() {
        return sharedPreferences.getBoolean(DARK_MODE_KEY, false);
    }

    // 🔹 Guardar el estado del modo oscuro
    public void setDarkMode(boolean isEnabled) {
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putBoolean(DARK_MODE_KEY, isEnabled);
        editor.apply();

        AppCompatDelegate.setDefaultNightMode(isEnabled ?
                AppCompatDelegate.MODE_NIGHT_YES :
                AppCompatDelegate.MODE_NIGHT_NO);
    }

    // 🔹 Obtener lista de productos favoritos
    public void getFavoriteItems(OnFavoriteItemsLoadedListener listener) {
        if (favRef == null) {
            listener.onLoaded(new ArrayList<>());
            return;
        }

        favRef.get().addOnSuccessListener(snapshot -> {
            List<Product> items = new ArrayList<>();
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

                    // 🔹 Verificar si ya hemos cargado todos los favoritos
                    if (items.size() == snapshot.getChildrenCount()) {
                        listener.onLoaded(items);
                    }
                }).addOnFailureListener(e -> listener.onLoaded(items));
            }
        }).addOnFailureListener(e -> listener.onLoaded(new ArrayList<>()));
    }

    // 🔹 Métodos para añadir/eliminar un favorito
    public void addFavorite(String productId) {
        if (favRef != null) {
            favRef.child(productId).setValue(true);
        }
    }

    public void removeFavorite(String productId) {
        if (favRef != null) {
            favRef.child(productId).removeValue();
        }
    }

    public interface OnFavoriteItemsLoadedListener {
        void onLoaded(List<Product> items);
    }
}
