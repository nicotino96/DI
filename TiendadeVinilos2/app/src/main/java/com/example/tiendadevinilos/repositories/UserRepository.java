package com.example.tiendadevinilos.repositories;

import static androidx.core.content.ContextCompat.startActivity;

import android.content.Intent;
import android.widget.Toast;

import androidx.lifecycle.MutableLiveData;

import com.example.tiendadevinilos.DashboardActivity;
import com.example.tiendadevinilos.LoginActivity;
import com.example.tiendadevinilos.models.User;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.concurrent.Executor;

public class UserRepository {
    private final FirebaseAuth auth;
    private final DatabaseReference database;

    public UserRepository() {
        auth = FirebaseAuth.getInstance();
        database = FirebaseDatabase.getInstance().getReference("users");
    }
    public interface LoginCallback {
        void onSuccess(FirebaseUser user);
        void onFailure(String errorMessage);
    }
    public MutableLiveData<Boolean> registerUser(String email, String password, String fullName, String phone, String address) {
        MutableLiveData<Boolean> registrationResult = new MutableLiveData<>();

        auth.createUserWithEmailAndPassword(email, password).addOnCompleteListener(task -> {
            if (task.isSuccessful()) {
                FirebaseUser user = auth.getCurrentUser();
                if (user != null) {
                    String userId = user.getUid();
                    database.child(userId).setValue(new User(fullName, email, phone, address))
                            .addOnCompleteListener(saveTask -> {
                                if (saveTask.isSuccessful()) {
                                    registrationResult.setValue(true);
                                } else {
                                    registrationResult.setValue(false);
                                }
                            });
                }
            } else {
                registrationResult.setValue(false);
            }
        });
        return registrationResult;
    }


    public FirebaseUser getCurrentUser() {
        return auth.getCurrentUser();
    }
    public void loginUser(String email, String password, LoginCallback callback) {
        if (email.isEmpty() || password.isEmpty()) {
            callback.onFailure("Por favor llena todos los campos.");
            return;
        }

        auth.signInWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        FirebaseUser user = auth.getCurrentUser();
                        callback.onSuccess(user);
                    } else {
                        String errorMessage = task.getException() != null
                                ? task.getException().getMessage()
                                : "Error en la autenticación.";
                        callback.onFailure(errorMessage);
                    }
                });
    }

    public void logoutUser() {
        auth.signOut();
    }
}
