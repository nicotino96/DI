package com.example.tiendadevinilos.views;

import android.content.Intent;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.core.view.GravityCompat;
import androidx.databinding.DataBindingUtil;
import androidx.fragment.app.Fragment;
import com.example.tiendadevinilos.R;
import com.example.tiendadevinilos.databinding.ActivityMainBinding;
import com.google.firebase.auth.FirebaseAuth;

public class MainActivity extends AppCompatActivity {

    private ActivityMainBinding binding;  // DataBinding

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Aplicar modo oscuro si está activado en preferencias
        applyDarkMode();

        // Usamos DataBinding para setear el layout
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main);

        // Manejamos los eventos del menú lateral
        binding.navigationView.setNavigationItemSelectedListener(item -> {
            int id = item.getItemId();

            if (id == R.id.nav_dashboard) {
                openFragment(new DashboardFragment());
            } else if (id == R.id.nav_favourites) {
                openFragment(new FavouritesFragment());
            } else if (id == R.id.nav_profile) {
                openFragment(new ProfileFragment());
            } else if (id == R.id.nav_logout) {
                logoutUser();
            }

            binding.drawerLayout.closeDrawer(GravityCompat.START); // Cierra el menú
            return true;
        });

        // Cargar el DashboardFragment por defecto
        if (savedInstanceState == null) {
            openFragment(new DashboardFragment());
            binding.navigationView.setCheckedItem(R.id.nav_dashboard);
        }
    }

    // Método para abrir un Fragment en el contenedor
    private void openFragment(Fragment fragment) {
        getSupportFragmentManager()
                .beginTransaction()
                .replace(R.id.fragmentContainer, fragment)
                .commit();
    }

    // Método para cerrar sesión
    private void logoutUser() {
        FirebaseAuth.getInstance().signOut();
        Intent intent = new Intent(this, LoginActivity.class);
        startActivity(intent);
        finish(); // Evita que vuelva con el botón atrás
    }

    // Método para aplicar el Modo Oscuro basado en SharedPreferences
    private void applyDarkMode() {
        boolean isDarkMode = getSharedPreferences("AppPrefs", MODE_PRIVATE)
                .getBoolean("dark_mode", false);

        AppCompatDelegate.setDefaultNightMode(
                isDarkMode ? AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO
        );
    }
}
