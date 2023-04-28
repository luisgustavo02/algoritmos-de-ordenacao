void bubblesort(int *v, int n){
    int i, j;
    for(i=0; i<n; i++){
        for(j=i; j<n-1; j++){
            if(v[j] > v[j+1]){
                int aux = v[j];
                v[j] = v[j+1];
                v[j+1] = aux;
            }
        }
    }
}
