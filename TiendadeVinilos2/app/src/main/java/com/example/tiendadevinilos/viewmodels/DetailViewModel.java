package com.example.tiendadevinilos.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.tiendadevinilos.repositories.FavoriteRepository;

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
        if (productId == null) return; // Evita llamadas con valores nulos

        repository.checkIfFavorite(productId, new FavoriteRepository.OnFavoriteCheckedListener() {
            @Override
            public void onChecked(boolean favorite) {
                isFavorite.postValue(favorite); // Se actualiza LiveData de forma segura en el hilo principal
            }
        });
    }

    public void toggleFavorite(String productId) {
        if (productId == null) return; // Evita llamadas con valores nulos

        boolean currentState = Boolean.TRUE.equals(isFavorite.getValue());
        isFavorite.setValue(!currentState);

        if (currentState) {
            repository.removeFavorite(productId);
        } else {
            repository.addFavorite(productId);
        }

        // La actualización se delega a Firebase y no se establece manualmente
        checkIfFavorite(productId);
    }
}