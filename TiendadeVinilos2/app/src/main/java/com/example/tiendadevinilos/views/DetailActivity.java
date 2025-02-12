package com.example.tiendadevinilos.views;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.lifecycle.ViewModelProvider;
import com.bumptech.glide.Glide;
import com.example.tiendadevinilos.R;
import com.example.tiendadevinilos.databinding.ActivityDetailBinding;
import com.example.tiendadevinilos.viewmodels.DetailViewModel;

public class DetailActivity extends AppCompatActivity {
    private ActivityDetailBinding binding;
    private DetailViewModel viewModel;
    private String productId;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityDetailBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        viewModel = new ViewModelProvider(this).get(DetailViewModel.class);

        // Obtener datos pasados desde DashboardActivity
        productId = getIntent().getStringExtra("id");
        String title = getIntent().getStringExtra("title");
        String description = getIntent().getStringExtra("description");
        String imageUrl = getIntent().getStringExtra("imageUrl");

        // Asignar datos a la vista
        binding.productTitle.setText(title);
        binding.productDescription.setText(description);
        Glide.with(this).load(imageUrl).into(binding.productImage);



        // Manejar clic en el botón de favoritos
        binding.fabFavorite.setOnClickListener(v -> {
            viewModel.toggleFavorite(productId); // Alternar favorito
        });
        // Verificar si es favorito
        viewModel.checkIfFavorite(productId);
        viewModel.getIsFavorite().observe(this, isFav -> {
            Log.d("DetailActivity", "Favorite state changed to: " + isFav);
            binding.fabFavorite.setImageDrawable(
                    ContextCompat.getDrawable(this,
                            Boolean.TRUE.equals(isFav) ?
                                    R.drawable.ic_favorite_border :
                                    R.drawable.ic_favorite
                    )
            );
        });
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        viewModel.getIsFavorite().removeObservers(this);
    }
}
