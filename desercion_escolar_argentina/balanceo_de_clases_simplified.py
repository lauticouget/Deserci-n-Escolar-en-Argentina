import pandas
from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import AllKNN

# Ver head del preprocessed.csv
df = pandas.read_csv("data/preprocessed/preprocessed_dataset.csv")
print(df.head())


# Asigno todas las columnas menos DESERTO como variables explicativas variable_explicada_df a DESERTO como variable explicada

# se extrajo la columna
df = df.drop(13745, axis="index")
print(df.value_counts("II8"))
print(df.head())
variables_explicativas_df = df.drop(["CODUSU", "MAS_500"], axis="columns")
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
        f"data/stage/df_resampled_oversampled_{round(muestra_minoritaria,2)}.csv",
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
        f"data/stage/df_resampled_undersampled_{round(muestra_minoritaria,2)}.csv",
        sep=",",
        index=False,
        encoding="utf-8",
    )

    muestra_minoritaria = muestra_minoritaria + 0.05
    muestra_mayoritaria = muestra_mayoritaria - 0.05


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