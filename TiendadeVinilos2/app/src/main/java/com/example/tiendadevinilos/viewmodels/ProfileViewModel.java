package com.example.tiendadevinilos.viewmodels;

import android.app.Application;
import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.example.tiendadevinilos.models.Product;
import com.example.tiendadevinilos.repositories.ProfileRepository;

import java.util.List;

public class ProfileViewModel extends AndroidViewModel {
    private final ProfileRepository profileRepository;
    private final MutableLiveData<Boolean> darkModeLiveData = new MutableLiveData<>();
    private final MutableLiveData<String> passwordChangeResult = new MutableLiveData<>();
    private final MutableLiveData<List<Product>> favorites = new MutableLiveData<>();


    public ProfileViewModel(@NonNull Application application) {
        super(application);
        profileRepository = new ProfileRepository(application);
        darkModeLiveData.setValue(profileRepository.isDarkModeEnabled());
    }

    // LiveData para observar cambios en el modo oscuro
    public LiveData<Boolean> getDarkModeLiveData() {
        return darkModeLiveData;
    }

    // LiveData para observar el resultado del cambio de contraseña
    public LiveData<String> getPasswordChangeResult() {
        return passwordChangeResult;
    }

    // Método para cambiar la contraseña
    public void changePassword(String newPassword) {
        profileRepository.changePassword(newPassword, new ProfileRepository.OnPasswordChangeListener() {
            @Override
            public void onSuccess() {
                passwordChangeResult.setValue("Contraseña cambiada correctamente.");
            }

            @Override
            public void onFailure(String errorMessage) {
                passwordChangeResult.setValue(errorMessage);
            }
        });
    }

    // Método para cambiar el modo oscuro
    public void toggleDarkMode(boolean isEnabled) {
        profileRepository.setDarkMode(isEnabled);
        darkModeLiveData.setValue(isEnabled);
    }
    public LiveData<List<Product>> getFavorites() {
        return favorites;
    }

    public void loadFavorites() {
        profileRepository.getFavoriteItems(favorites::setValue);
    }

    public void toggleFavorite(String productId) {
        if (favorites.getValue() != null && favorites.getValue().stream().anyMatch(p -> p.getId().equals(productId))) {
            profileRepository.removeFavorite(productId);
        } else {
            profileRepository.addFavorite(productId);
        }
        loadFavorites(); // Refrescar la lista después de actualizar
    }
}
