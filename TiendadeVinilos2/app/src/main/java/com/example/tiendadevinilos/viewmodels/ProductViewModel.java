package com.example.tiendadevinilos.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.tiendadevinilos.models.Product;
import com.example.tiendadevinilos.repositories.ProductRepository;

import java.util.List;

public class ProductViewModel extends ViewModel {
    private final MutableLiveData<List<Product>> productLiveData = new MutableLiveData<>();
    private final ProductRepository productRepository;

    public ProductViewModel() {
        productRepository = new ProductRepository();
        loadProducts();
    }

    public LiveData<List<Product>> getProductLiveData() {
        return productLiveData;
    }

    private void loadProducts() {
        productRepository.getProducts(productLiveData);
    }
}
