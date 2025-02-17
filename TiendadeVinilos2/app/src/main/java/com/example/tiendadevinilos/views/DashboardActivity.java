package com.example.tiendadevinilos.views;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.tiendadevinilos.R;
import com.example.tiendadevinilos.adapters.ProductAdapter;
import com.example.tiendadevinilos.databinding.ActivityDashboardBinding;
import com.example.tiendadevinilos.viewmodels.DashboardViewModel;

import java.util.ArrayList;

public class DashboardActivity extends AppCompatActivity {

    private ProductAdapter productAdapter;
    private DashboardViewModel dashboardViewModel;
    private ActivityDashboardBinding binding;
    private SharedPreferences sharedPreferences;
    private static final String PREFS_NAME = "AppPrefs";
    private static final String DARK_MODE_KEY = "dark_mode";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        sharedPreferences = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        boolean isDarkMode = sharedPreferences.getBoolean(DARK_MODE_KEY, false);
        if (isDarkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }

        // Enlazar el layout con DataBinding
        binding = DataBindingUtil.setContentView(this, R.layout.activity_dashboard);

        // Set accessibility descriptions for buttons
        binding.logoutButton.setContentDescription(getString(R.string.logout_button_description));
        binding.fabFavorites.setContentDescription(getString(R.string.favorites_button_description));

        // Configurar ViewModel y RecyclerView
        dashboardViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);
        productAdapter = new ProductAdapter(new ArrayList<>(), product -> {
            Intent intent = new Intent(this, DetailActivity.class);
            intent.putExtra("id", product.getId());
            intent.putExtra("title", product.getTitle());
            intent.putExtra("description", product.getDescription());
            intent.putExtra("imageUrl", product.getImageUrl());

            // Add accessibility announcement before navigation
            binding.recyclerView.announceForAccessibility(
                    getString(R.string.opening_product_details, product.getTitle())
            );

            startActivity(intent);
        });

        // Observador del ViewModel
        dashboardViewModel.getProductsLiveData().observe(this, products -> {
            if (products != null) {
                productAdapter.setProductList(products);
                // Announce products loaded for accessibility
                binding.recyclerView.announceForAccessibility(
                        getString(R.string.products_loaded_description)
                );
            } else {
                Toast.makeText(this, R.string.error_loading_products, Toast.LENGTH_SHORT).show();
                binding.recyclerView.announceForAccessibility(
                        getString(R.string.error_loading_products)
                );
            }
        });

        binding.recyclerView.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerView.setAdapter(productAdapter);

        // Set click listeners with accessibility feedback
        binding.logoutButton.setOnClickListener(v -> {
            binding.logoutButton.announceForAccessibility(
                    getString(R.string.logging_out_description)
            );
            Intent intent = new Intent(DashboardActivity.this, LoginActivity.class);
            startActivity(intent);
            finish();
        });

        binding.darkModeToggle.setChecked(isDarkMode);
        binding.darkModeToggle.setOnCheckedChangeListener((buttonView, isChecked) -> {
            // Guardar preferencia del modo oscuro
            SharedPreferences.Editor editor = sharedPreferences.edit();
            editor.putBoolean(DARK_MODE_KEY, isChecked);
            editor.apply();

            // Aplicar el tema y reiniciar la actividad
            if (isChecked) {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
            } else {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
            }
            recreate(); // Recargar la actividad para aplicar cambios
        });

        binding.fabFavorites.setOnClickListener(v -> {
            binding.fabFavorites.announceForAccessibility(
                    getString(R.string.opening_favorites_description)
            );
            Intent intent = new Intent(DashboardActivity.this, FavouritesActivity.class);
            startActivity(intent);
        });
    }
}