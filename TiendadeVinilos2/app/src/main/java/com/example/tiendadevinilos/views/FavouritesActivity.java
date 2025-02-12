package com.example.tiendadevinilos.views;

import android.content.Intent;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import com.example.tiendadevinilos.adapters.ProductAdapter;
import com.example.tiendadevinilos.databinding.ActivityFavouritesBinding;
import com.example.tiendadevinilos.models.Product;
import com.example.tiendadevinilos.viewmodels.FavouritesViewModel;
import java.util.ArrayList;
import java.util.List;

public class FavouritesActivity extends AppCompatActivity {
    private ActivityFavouritesBinding binding;
    private FavouritesViewModel viewModel;
    private ProductAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityFavouritesBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        viewModel = new ViewModelProvider(this).get(FavouritesViewModel.class);

        // Configurar RecyclerView con el adaptador
        adapter = new ProductAdapter(new ArrayList<>(), product -> {
            Intent intent = new Intent(FavouritesActivity.this, DetailActivity.class);
            intent.putExtra("id", product.getId());
            intent.putExtra("title", product.getTitle());
            intent.putExtra("description", product.getDescription());
            intent.putExtra("imageUrl", product.getImageUrl());
            startActivity(intent);
        });

        binding.recyclerView.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerView.setAdapter(adapter);

        // Observar cambios en los favoritos
        viewModel.getFavorites().observe(this, adapter::setProductList);
    }
}