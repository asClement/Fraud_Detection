# Features de modélisation - notebook 1.1-modeling

Ce fichier recense les colonnes présentes au départ dans le notebook, puis les features construites pour la modélisation. Les formules ci-dessous reprennent exactement la logique appliquée dans le notebook.

## Variables brutes du dataset de départ

Le `train.csv` contient les colonnes suivantes au début du notebook :

- `id`
- `period`
- `operation`
- `amount`
- `origin_account`
- `origin_balance_before`
- `origin_balance_after`
- `destination_account`
- `destination_balance_before`
- `destination_balance_after`
- `fraud_flag` uniquement dans l’entraînement

## Features créées pour la modélisation

### `type`
Indique si l’opération ressemble à un débit ou à un crédit à partir des soldes du compte d’origine.

$$
type = \mathbb{1}\big[origin\_balance\_before < 0 \land origin\_balance\_after > 0\big]
$$

### `orig_balance_check`
Vérifie si le solde du compte d’origine suit la règle attendue selon le type d’opération.

$$
orig\_balance\_check = \mathbb{1}\Big[
(type = 0 \land origin\_balance\_after = origin\_balance\_before - amount)
\lor
(type = 1 \land origin\_balance\_after = origin\_balance\_before + amount)
\Big]
$$

### `error_origin_balance`
Mesure l’écart absolu entre le solde d’origine attendu et le solde observé, puis applique un log pour compresser les grandes valeurs.

$$
error\_origin\_balance =
\begin{cases}
\log(1 + |(origin\_balance\_before - amount) - origin\_balance\_after|), & \text{si } type = 0 \\
\log(1 + |(origin\_balance\_before + amount) - origin\_balance\_after|), & \text{si } type = 1
\end{cases}
$$

### `dest_balance_check`
Vérifie si le solde du compte de destination est cohérent avec le montant transféré et le type d’opération.

$$
dest\_balance\_check = \mathbb{1}\Big[
(type = 0 \land destination\_balance\_after = destination\_balance\_before + amount)
\lor
(type = 1 \land destination\_balance\_after = destination\_balance\_before)
\Big]
$$

### `error_destination_balance`
Mesure l’écart entre le solde de destination attendu et le solde observé, puis applique un log pour réduire l’effet des valeurs extrêmes.

$$
error\_destination\_balance =
\begin{cases}
\log(1 + |(destination\_balance\_before + amount) - destination\_balance\_after|), & \text{si } type = 0 \\
\log(1 + |destination\_balance\_before - destination\_balance\_after|), & \text{si } type = 1
\end{cases}
$$

### `was_transfert_blocked_before`
Indique si le compte d’origine n’a pas bougé après l’opération.

$$
was\_transfert\_blocked\_before = \mathbb{1}[origin\_balance\_before = origin\_balance\_after]
$$

### `was_transfert_blocked_after`
Indique si le compte de destination n’a pas bougé après l’opération.

$$
was\_transfert\_blocked\_after = \mathbb{1}[destination\_balance\_before = destination\_balance\_after]
$$

### `is_op_03`
Repère directement les transactions de type `op_03`.

$$
is\_op\_03 = \mathbb{1}[operation = op\_03]
$$

### `log_amount`
Applique une transformation logarithmique au montant pour réduire l’asymétrie de la distribution.

$$
log\_amount = \log(1 + amount)
$$

### `amount_class`
Crée une classe binaire en comparant le montant transformé à la moyenne de `log_amount`.

$$
amount\_class = \mathbb{1}[log\_amount > \mu_{split}(log\_amount)]
$$

### `prd_catg`
Repère les périodes dont les opérations observées sont uniquement `op_03` et `op_05`.

$$
prd\_catg = \mathbb{1}[\{operation\_sur\_la\_periode\} = \{op\_03, op\_05\}]
$$

### `orig_balance_before_amount_ratio`
Construit un ratio entre le solde d’origine avant transaction et le montant, puis applique un log sur la valeur absolue arrondie.

$$
orig\_balance\_before\_amount\_ratio = \log\big(1 + |\mathrm{round}(origin\_balance\_before / amount, 4)|\big)
$$

### `dest_balance_after_amount_ratio`
Construit un ratio entre le solde de destination après transaction et le montant, puis applique un log sur la valeur absolue arrondie.

$$
dest\_balance\_after\_amount\_ratio = \log\big(1 + |\mathrm{round}(destination\_balance\_after / amount, 4)|\big)
$$

### `operation` encodée
La variable catégorielle `operation` est transformée en entier par encodage ordinal.

$$
operation_{enc} = \mathrm{LabelEncoder}(operation)
$$

## Variables retenues dans l’entraînement

Le vecteur `FEATURES` conserve toutes les colonnes utiles pour le modèle, sauf les identifiants et la cible : `id`, `period`, `origin_account`, `destination_account`, `fraud_flag`.

En pratique, les features d’entrée sont :

- `operation` encodée
- `amount`
- `origin_balance_before`
- `origin_balance_after`
- `destination_balance_before`
- `destination_balance_after`
- `type`
- `orig_balance_check`
- `error_origin_balance`
- `dest_balance_check`
- `error_destination_balance`
- `was_transfert_blocked_before`
- `was_transfert_blocked_after`
- `is_op_03`
- `log_amount`
- `amount_class`
- `prd_catg`
- `orig_balance_before_amount_ratio`
- `dest_balance_after_amount_ratio`

## Colonnes ajoutées après modélisation

Les colonnes `xgb_target`, `lgbm_target`, `catboost_target` et `target` servent à stocker les probabilités de sortie des modèles et leur moyenne, mais ne font pas partie des features d’apprentissage.
