package com.example.tiendadevinilos.views;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import com.example.tiendadevinilos.databinding.FragmentProfileBinding;
import com.example.tiendadevinilos.viewmodels.ProfileViewModel;

public class ProfileFragment extends Fragment {
    private FragmentProfileBinding binding;
    private ProfileViewModel profileViewModel;

    public ProfileFragment() {
        // Constructor vacío requerido
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        binding = FragmentProfileBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // Inicializar ViewModel
        profileViewModel = new ViewModelProvider(this).get(ProfileViewModel.class);

        // Observar cambios en el modo oscuro
        profileViewModel.getDarkModeLiveData().observe(getViewLifecycleOwner(), isDarkMode ->
                binding.darkModeToggle.setChecked(isDarkMode)
        );

        // Toggle de Dark Mode
        binding.darkModeToggle.setOnCheckedChangeListener((buttonView, isChecked) ->
                profileViewModel.toggleDarkMode(isChecked)
        );

        // Manejar cambio de contraseña
        binding.changePasswordButton.setOnClickListener(v -> {
            String newPassword = binding.newPasswordEditText.getText().toString().trim();
            if (newPassword.isEmpty()) {
                Toast.makeText(requireContext(), "Ingrese una nueva contraseña", Toast.LENGTH_SHORT).show();
                return;
            }
            profileViewModel.changePassword(newPassword);
        });

        // Observar resultado del cambio de contraseña
        profileViewModel.getPasswordChangeResult().observe(getViewLifecycleOwner(), result ->
                Toast.makeText(requireContext(), result, Toast.LENGTH_SHORT).show()
        );
    }
}
