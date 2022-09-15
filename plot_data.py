# Select all numeric variables
num_variables = my_sample_na_mean \
    .select_dtypes(include=[np.number]).columns.tolist()
