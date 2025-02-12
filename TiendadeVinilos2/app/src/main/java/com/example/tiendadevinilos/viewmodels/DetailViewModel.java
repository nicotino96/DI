package com.example.tiendadevinilos.viewmodels;

import android.util.Log;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.tiendadevinilos.repositories.FavoriteRepository;
import com.example.tiendadevinilos.repositories.UserRepository;
import com.google.android.gms.tasks.Task;

public class DetailViewModel extends ViewModel {
    private final FavoriteRepository repository;
    private final MutableLiveData<Boolean> isFavorite = new MutableLiveData<>(false); // Estado inicial en falso

    public DetailViewModel() {
        repository = new FavoriteRepository();
    }

    public LiveData<Boolean> getIsFavorite() {
        return isFavorite;
    }

    public void checkIfFavorite(String productId) {
        if (productId == null) return;

        repository.checkIfFavorite(productId, new FavoriteRepository.OnFavoriteCheckedListener() {
            @Override
            public void onChecked(boolean favorite) {
                isFavorite.postValue(favorite); // Asegura que la UI reciba la actualización
            }
        });
    }

    public void toggleFavorite(String productId) {
        if (productId == null) return;

        boolean newState = !Boolean.TRUE.equals(isFavorite.getValue());
        Log.d("DetailViewModel", "Toggling favorite to: " + newState);

        Task<Void> task;
        if (newState) {
            task = repository.addFavorite(productId);
        } else {
            task = repository.removeFavorite(productId);
        }

        task.addOnSuccessListener(aVoid -> {
            Log.d("DetailViewModel", "Firebase operation successful");
            isFavorite.setValue(newState);
        }).addOnFailureListener(e -> {
            Log.e("DetailViewModel", "Firebase operation failed", e);
        });
    }
}