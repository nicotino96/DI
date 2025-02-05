package com.example.tiendadevinilos.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.tiendadevinilos.models.Product;
import com.example.tiendadevinilos.repositories.ProductRepository;

import java.util.List;

/**
 * ViewModel para el dashboard de la aplicación.
 * Emplea el repositorio de aves para obtener la lista de aves
 * y la mantiente actualizada en tiempo real.
 */
public class DashboardViewModel extends ViewModel {
    private final MutableLiveData<List<Product>> productsLiveData = new MutableLiveData<>();
    private final ProductRepository productRepository;
    private final MutableLiveData<Product> selectedProduct = new MutableLiveData<>();

    public DashboardViewModel() {
        productRepository = new ProductRepository();
        loadProducts();
    }
    public MutableLiveData<List<Product>> getProductsLiveData() {
        return productsLiveData;
    }

    private void selectProduct(Product product) {
        productRepository.getProducts(productsLiveData);
    }
    private void loadProducts() {
        productRepository.getProducts(productsLiveData);
    }
    public LiveData<Product> getSelectedRecipe() {
        return selectedProduct;
    }
}