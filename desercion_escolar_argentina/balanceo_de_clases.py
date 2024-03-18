import pandas
from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import AllKNN

# Ver head del preprocessed.csv

df = pandas.read_csv("data/preprocessed/preprocessed_codificacion.csv")
print(df.head())


# Asigno todas las columnas menos DESERTO como variables explicativas variable_explicada_df a DESERTO como variable explicada


print(df.head())
variables_explicativas_df = df.drop(["MAS_500"], axis="columns")
print(variables_explicativas_df)

variable_explicada_df = df.loc[:, "DESERTO"]
print(variable_explicada_df)


# Hago loop con minoritaria a 0.2 hasta 0.5 de la mayoritaria

muestra_minoritaria = 0.2
muestra_mayoritaria = 0.8

for i in range(7):
    # Establezco la sampling strategy
    sampling_strategy = round(muestra_minoritaria / muestra_mayoritaria, 2)
    print(sampling_strategy)

    # Probamos primero con un Oversampling estandar
    df_resampled_oversampled, variable_explicada_df_resampled = RandomOverSampler(
        sampling_strategy=sampling_strategy
    ).fit_resample(variables_explicativas_df, variable_explicada_df)
    df_resampled_oversampled = pandas.DataFrame(df_resampled_oversampled)

    # Printeo el head para ver como se guardará
    print(df_resampled_oversampled.head())

    # Guardo como CSV cada muestra resampleada con el método correspondiente
    df_resampled_oversampled.to_csv(
        f"data/stage/df_resampled_oversampled_escalado_{round(muestra_minoritaria,2)}.csv",
        sep=",",
        index=False,
        encoding="utf-8",
    )
    # Aplicamos Metodo SMOTE
    df_resampled_SMOTE, variable_explicada_df_SMOTE = SMOTE(
        sampling_strategy=sampling_strategy
    ).fit_resample(variables_explicativas_df, variable_explicada_df)
    df_resampled_SMOTE = pandas.DataFrame(df_resampled_SMOTE)

    # Printeo el head para ver como se guardará
    print(df_resampled_SMOTE.head())

    # Guardo como CSV cada muestra resampleada con el método correspondiente
    df_resampled_SMOTE.to_csv(
        f"data/stage/df_resampled_SMOTE_escalado_{round(muestra_minoritaria,2)}.csv",
        sep=",",
        index=False,
        encoding="utf-8",
    )

    # Aplicamos Metodo ADASYN
    df_resampled_ADASYN, variable_explicada_df_ADASYN = ADASYN(
        sampling_strategy=sampling_strategy
    ).fit_resample(variables_explicativas_df, variable_explicada_df)
    df_resampled_ADASYN = pandas.DataFrame(df_resampled_ADASYN)

    # Printeo el head para ver como se guardará
    print(df_resampled_ADASYN.head())

    # Guardo como CSV cada muestra resampleada con el método correspondiente
    df_resampled_ADASYN.to_csv(
        f"data/stage/df_resampled_ADASYN_escalado_{round(muestra_minoritaria,2)}.csv",
        sep=",",
        index=False,
        encoding="utf-8",
    )
    # Probamos primero con un Undersampling estandar
    df_resampled_undersampled, variable_explicada_df_undersampled = RandomUnderSampler(
        sampling_strategy=sampling_strategy
    ).fit_resample(variables_explicativas_df, variable_explicada_df)
    df_resampled_undersampled = pandas.DataFrame(df_resampled_undersampled)

    # Printeo el head para ver como se guardará
    print(df_resampled_undersampled.head())

    # Guardo como CSV cada muestra resampleada con el método correspondiente
    df_resampled_undersampled.to_csv(
        f"data/stage/df_resampled_undersampled_escalado_{round(muestra_minoritaria,2)}.csv",
        sep=",",
        index=False,
        encoding="utf-8",
    )

    muestra_minoritaria = muestra_minoritaria + 0.05
    muestra_mayoritaria = muestra_mayoritaria - 0.05

# Probamos con un Undersampling AllKNN
df_resampled_AllKNN, variable_explicada_df_AllKNN = AllKNN().fit_resample(
    variables_explicativas_df, variable_explicada_df
)
df_resampled_AllKNN = pandas.DataFrame(df_resampled_AllKNN)

# Printeo el head para ver como se guardará
print(df_resampled_AllKNN.head())

# Guardo como CSV cada muestra resampleada con el método correspondiente
df_resampled_AllKNN.to_csv(
    f"data/stage/df_resampled_AllKNN_escalado.csv",
    sep=",",
    index=False,
    encoding="utf-8",
)

"""df2.to_csv(
    "./data/balanceo_de_clases_oversampled.csv",
    sep=",",
    index=False,
    encoding="utf-8",
)
"""
"""
# Crear el objeto SMOTE variable_explicada_df ADASYN
SMOTE = SMOTE()
ADASYN = ADASYN()

# Aplicar SMOTE a tus datos
df_resampled_oversampled, variable_explicada_df_resampled = (
    SMOTE.fit_resample(variables_explicativas_df, variable_explicada_df)
)

clf_SMOTE = LogisticRegression().fit(
    df_resampled_oversampled, variable_explicada_df_resampled
)
df_resampled_oversampled, variable_explicada_df_resampled = (
    ADASYN.fit_resample(variables_explicativas_df, variable_explicada_df)
)

clf_ADASYN = LogisticRegression().fit(
    df_resampled_oversampled, variable_explicada_df_resampled
)
"""
""" # Probamos con un Undersampling AllKNN
    df_resampled_AllKNN, variable_explicada_df_AllKNN = AllKNN(
        sampling_strategy=sampling_strategy
    ).fit_resample(variables_explicativas_df, variable_explicada_df)
    df_resampled_AllKNN = pandas.DataFrame(df_resampled_AllKNN)

    # Printeo el head para ver como se guardará
    print(df_resampled_AllKNN.head())

    # Guardo como CSV cada muestra resampleada con el método correspondiente
    df_resampled_AllKNN.to_csv(
        f"data/stage/df_resampled_AllKNN_escalado_{round(muestra_minoritaria,2)}.csv",
        sep=",",
        index=False,
        encoding="utf-8",
    )
"""