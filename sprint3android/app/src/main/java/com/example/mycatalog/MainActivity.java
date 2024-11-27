package com.example.mycatalog;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.navigation.fragment.NavHostFragment;
import androidx.navigation.ui.NavigationUI;

import com.google.android.material.bottomnavigation.BottomNavigationView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Llamada al método onCreate de la superclase para inicializar la actividad
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Configura la navegación con la barra inferior
        setupNavegacion();
    }

    /**
     * Configura la navegación utilizando un NavHostFragment y un BottomNavigationView.
     */
    private void setupNavegacion() {
        // Barra de navegación inferior
        BottomNavigationView bottomNavigationView = findViewById(R.id.bottomNavigationView);

        // Fragmento de navegación (NavHostFragment)
        NavHostFragment navHostFragment = (NavHostFragment) getSupportFragmentManager().findFragmentById(R.id.nav_hostfragment);

        // Vincula el controlador de navegación con la barra de navegación inferior
        NavigationUI.setupWithNavController(
                bottomNavigationView,
                navHostFragment.getNavController());
    }
}