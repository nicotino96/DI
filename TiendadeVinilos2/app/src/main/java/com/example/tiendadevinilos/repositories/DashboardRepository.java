package com.example.tiendadevinilos.repositories;

import com.example.tiendadevinilos.models.Product;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class DashboardRepository {

    private DatabaseReference mDatabase;

    public DashboardRepository() {
        mDatabase = FirebaseDatabase.getInstance().getReference();
    }

    public void loadGames(OnDataLoadedListener listener) {
        mDatabase.child("item").addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                List<Product> products = new ArrayList<>();
                for (DataSnapshot snapshot : dataSnapshot.getChildren()) {
                    Product product = snapshot.getValue(Product.class);
                    product.setId(snapshot.getKey());
                    if (product != null) {
                        products.add(product);

                    }
                }
                listener.onDataLoaded(products);
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                listener.onDataFailed(databaseError.toException());
            }
        });
    }

    public interface OnDataLoadedListener {
        void onDataLoaded(List<Product> games);
        void onDataFailed(Exception e);
    }
}
