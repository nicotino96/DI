package com.example.tiendadevinilos.viewmodels;

import android.util.Log;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.tiendadevinilos.repositories.FavoriteRepository;
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
        if (productId == null || productId.isEmpty()) {
            Log.e("DetailViewModel", "Error: productId es nulo o vacío.");
            return;
        }

        repository.checkIfFavorite(productId, isFav -> {
            Log.d("DetailViewModel", "Producto " + productId + " es favorito: " + isFav);
            isFavorite.postValue(isFav); // 🔹 Asegurar actualización en el hilo correcto
        });
    }

    public void toggleFavorite(String productId) {
        if (productId == null || productId.isEmpty()) {
            Log.e("DetailViewModel", "Error: productId es nulo o vacío.");
            return;
        }

        boolean newState = !Boolean.TRUE.equals(isFavorite.getValue());
        Log.d("DetailViewModel", "Toggling favorite for " + productId + " to: " + newState);

        Task<Void> task = newState ? repository.addFavorite(productId) : repository.removeFavorite(productId);

        task.addOnSuccessListener(aVoid -> {
            Log.d("DetailViewModel", "Operación en Firebase exitosa");
            isFavorite.postValue(newState); // 🔹 Evitar conflictos de hilo
        }).addOnFailureListener(e -> {
            Log.e("DetailViewModel", "Error en la operación de Firebase", e);
        });
    }
}
