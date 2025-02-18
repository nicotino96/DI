package com.example.tiendadevinilos.repositories;

import android.content.Context;
import android.content.SharedPreferences;
import androidx.appcompat.app.AppCompatDelegate;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class ProfileRepository {
    private static final String PREFS_NAME = "AppPrefs";
    private static final String DARK_MODE_KEY = "dark_mode";

    private final FirebaseAuth auth;
    private final SharedPreferences sharedPreferences;

    public ProfileRepository(Context context) {
        auth = FirebaseAuth.getInstance();
        sharedPreferences = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
    }

    // Cambiar contraseña del usuario autenticado
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

    // Obtener el estado del modo oscuro
    public boolean isDarkModeEnabled() {
        return sharedPreferences.getBoolean(DARK_MODE_KEY, false);
    }

    // Guardar el estado del modo oscuro
    public void setDarkMode(boolean isEnabled) {
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putBoolean(DARK_MODE_KEY, isEnabled);
        editor.apply();
        AppCompatDelegate.setDefaultNightMode(isEnabled ?
                AppCompatDelegate.MODE_NIGHT_YES :
                AppCompatDelegate.MODE_NIGHT_NO);
    }
}
