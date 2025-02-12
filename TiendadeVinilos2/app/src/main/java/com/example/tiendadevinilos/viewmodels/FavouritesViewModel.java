package com.example.tiendadevinilos.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.tiendadevinilos.models.Product;
import com.example.tiendadevinilos.repositories.FavoriteRepository;
import java.util.List;

public class FavouritesViewModel extends ViewModel {
    private final FavoriteRepository repository;
    private final MutableLiveData<List<Product>> favoriteItems = new MutableLiveData<>();

    public FavouritesViewModel() {
        repository = new FavoriteRepository();
        loadFavorites();
    }

    public LiveData<List<Product>> getFavorites() {
        return favoriteItems;
    }

    private void loadFavorites() {
        repository.getFavoriteItems(favoriteItems::setValue);
    }
}