package com.example.tiendadevinilos.repositories;

import androidx.lifecycle.MutableLiveData;

import com.example.tiendadevinilos.models.User;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class UserRepository {
    private final FirebaseAuth auth;
    private final DatabaseReference database;

    public UserRepository() {
        auth = FirebaseAuth.getInstance();
        database = FirebaseDatabase.getInstance().getReference("users");
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
}
