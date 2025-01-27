package com.example.tiendadevinilos.viewmodels;

import android.widget.Toast;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.tiendadevinilos.repositories.UserRepository;

public class RegisterViewModel extends ViewModel {
    private final UserRepository userRepository;
    private final MutableLiveData<Boolean> registrationSuccess = new MutableLiveData<>();
    private final MutableLiveData<String> registrationError = new MutableLiveData<>();

    public RegisterViewModel() {
        userRepository = new UserRepository();
    }

    public LiveData<Boolean> getRegistrationSuccess() {
        return registrationSuccess;
    }

    public LiveData<String> getRegistrationError() {
        return registrationError;
    }

    public void registerUser(String email, String password, String confirmPassword, String fullName, String phone, String address) {
        if (email.isEmpty() || password.isEmpty() || fullName.isEmpty() || phone.isEmpty() || address.isEmpty()) {
            registrationError.setValue("All fields are required.");
            return;
        }

        if (password.length() < 6) {
            registrationError.setValue("Password must be at least 6 characters.");
            return;
        }
        if (!email.contains("@")) {
            registrationError.setValue("Invalid email address.");
            return;
        }
        if (!password.equals(confirmPassword)) {
            registrationError.setValue("Passwords do not match.");
            return;
        }

        userRepository.registerUser(email, password, fullName, phone, address).observeForever(success -> {
            if (success) {
                registrationSuccess.setValue(true);
            } else {
                registrationError.setValue("Registration failed. Try again.");
            }
        });
    }
}
