/**
 * A library of functions to help with plot creation.
 */

// A map of {string to search for: string to categorize into}
val COMMON_INGREDIENTS: Map<String, String> = mapOf(
    "flour" to " cups flour",
    "baking soda" to " teaspoons baking soda",
    "baking powder" to " teaspoons baking powder",
    "salt" to " teaspoons salt",
    "egg" to " eggs",
    "butter" to " cups butter/margarine",
    "margarine" to " cups butter/margarine",
    "sugar" to " cups sugar",
    "oil" to " cups oil",
    "milk" to " cups milk",
    "vanilla" to " teaspoons vanilla extract",
    "cinnamon" to " tablespoons cinnamon",
    "chocolate chips" to " cups chocolate chips",
    "oatmeal" to " cups oatmeal",
    "rolled oats" to " cups oatmeal",
    "quick cooking oats" to " cups oatmeal",
    "raisins" to " cups raisins"
)

// A map of {ingredient as it appears in recipe: unit}
val COMMON_INGREDIENT_UNITS: Map<String, String> = mapOf(
    " cups flour" to "cups",
    " teaspoons baking soda" to "teaspoons",
    " teaspoons baking powder" to "teaspoons",
    " teaspoons salt" to "teaspoons",
    " eggs" to "eggs",
    " cups butter/margarine" to "cups",
    " cups sugar" to "cups",
    " cups oil" to "cups",
    " cups milk" to "cups",
    " teaspoons vanilla extract" to "teaspoons",
    " tablespoons cinnamon" to "tablespoons",
    " cups chocolate chips" to "cups",
    " cups oatmeal" to "cups",
    " cups raisins" to "cups"
)

/**
 * Combine common ingredients that are the same but formatted differently.
 *
 * Search for keywords such as "flour" in the ingredient description.
 *
 * This function just combines ingredients and doesn't also run
 * take_average_ingredients as a step of calculate_average_recipe
 * like the version in average_recipe does.
 *
 * @param ingredientsDictUncombined a map representing the ingredients
 * and amounts in the recipe, with repeat ingredients not combined.
 *
 * @return a map representing the ingredients and amounts with
 * ingredients that are the same combined together.
 */
fun combineSameIngredientsStandalone(
    ingredientsDictUncombined: Map<String, Double>
): Map<String, Double> {

    val ingredientsDictCombined: MutableMap<String, Double> = mutableMapOf(
        " cups flour" to 0.0,
        " teaspoons baking soda" to 0.0,
        " teaspoons baking powder" to 0.0,
        " teaspoons salt" to 0.0,
        " eggs" to 0.0,
        " cups butter/margarine" to 0.0,
        " cups sugar" to 0.0,
        " cups oil" to 0.0,
        " cups milk" to 0.0,
        " teaspoons vanilla extract" to 0.0,
        " tablespoons cinnamon" to 0.0,
        " cups chocolate chips" to 0.0,
        " cups oatmeal" to 0.0,
        " cups raisins" to 0.0
    )

    for ((ingredient: String, amount: Double) in ingredientsDictUncombined) {
        var ingredientFound: Boolean = false

        for ((searchString: String, finalIngredient: String) in COMMON_INGREDIENTS) {
            if (searchString in ingredient) {
                val currentAmount: Double =
                    ingredientsDictCombined[finalIngredient] ?: 0.0

                ingredientsDictCombined[finalIngredient] =
                    currentAmount + amount

                ingredientFound = true
                break
            }
        }

        if (!ingredientFound) {
            ingredientsDictCombined[ingredient] = amount
        }
    }

    return ingredientsDictCombined.filterValues { value: Double ->
        value != 0.0
    }
}

/**
 * Converts a list of ingredient lists in the same format into cups.
 *
 * Converts all common ingredients and deletes every uncommon ingredient.
 *
 * @param listIngredientsPerAllRecipes a list of strings representing
 * ingredients for each recipe.
 *
 * @return a map of ingredients and corresponding amounts in cups,
 * with uncommon ingredients deleted.
 */
fun convertToCups(
    listIngredientsPerAllRecipes: List<List<String>>
): Map<String, Double> {

    val ingredientsDict: Map<String, Double> =
        separateAmountsAndIngredients(listIngredientsPerAllRecipes)

    val combinedIngredients: Map<String, Double> =
        combineSameIngredientsStandalone(ingredientsDict)

    val ingredientsDictInCups: MutableMap<String, Double> =
        mutableMapOf()

    for ((ingredient: String, amount: Double) in combinedIngredients) {
        if (ingredient in COMMON_INGREDIENT_UNITS) {

            val unit: String? = COMMON_INGREDIENT_UNITS[ingredient]

            when (unit) {
                "cups" -> {
                    // Convert cups to cups, leave unchanged
                    ingredientsDictInCups[ingredient] = amount
                }

                "teaspoons" -> {
                    // Convert teaspoons to cups
                    // 1 teaspoon = 1/48 cup
                    ingredientsDictInCups[ingredient] = amount / 48.0
                }

                "tablespoons" -> {
                    // Convert tablespoons to cups
                    // 1 tablespoon = 1/16 cup
                    ingredientsDictInCups[ingredient] = amount / 16.0
                }

                "eggs" -> {
                    // Convert eggs to cups
                    // 1 egg = 1/4 cup
                    ingredientsDictInCups[ingredient] = amount / 4.0
                }
            }
        }
    }

    return ingredientsDictInCups
}
