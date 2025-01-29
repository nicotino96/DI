package com.example.tiendadevinilos.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.tiendadevinilos.repositories.UserRepository;
import com.google.firebase.auth.FirebaseUser;

public class LoginViewModel extends ViewModel {

    private final UserRepository userRepository;
    private final MutableLiveData<FirebaseUser> userLiveData = new MutableLiveData<>();
    private final MutableLiveData<String> errorLiveData = new MutableLiveData<>();

    public LoginViewModel() {
        this.userRepository = new UserRepository();
    }

    public LiveData<FirebaseUser> getUserLiveData() {
        return userLiveData;
    }

    public LiveData<String> getErrorLiveData() {
        return errorLiveData;
    }

    public void loginUser(String email, String password) {
        userRepository.loginUser(email, password, new UserRepository.LoginCallback() {
            @Override
            public void onSuccess(FirebaseUser user) {
                userLiveData.setValue(user);
            }

            @Override
            public void onFailure(String errorMessage) {
                errorLiveData.setValue(errorMessage);
            }
        });
    }
}
