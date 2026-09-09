/**
 * Test library for data processing functions related to making our plots.
 */

import kotlin.test.Test
import kotlin.test.assertEquals

class PythonToKotlinTest {

    private val combineSameIngredientsStandaloneCases = listOf(
        // A single ingredient written in standard form should return unchanged.
        Pair(
            mapOf(" cups sugar" to 1.0),
            mapOf(" cups sugar" to 1.0)
        ),

        // A single ingredient in improper form should be written in standard form.
        Pair(
            mapOf(" cup white sugar" to 1.0),
            mapOf(" cups sugar" to 1.0)
        ),

        // Two of the same ingredients should be combined together.
        Pair(
            mapOf(
                " cup white sugar" to 1.0,
                " cups sugar (granulated)" to 2.0
            ),
            mapOf(" cups sugar" to 3.0)
        ),

        // A dict with only an uncommon ingredient should return itself.
        Pair(
            mapOf(" cups meatloaf" to 3.0),
            mapOf(" cups meatloaf" to 3.0)
        )
    )

    private val convertToCupsCases = listOf(
        // A single ingredient in cups and written in standard form should return
        // unchanged.
        Pair(
            listOf(listOf("1 cups sugar")),
            mapOf(" cups sugar" to 1.0)
        ),

        // A single ingredient not in cups should return itself in cups.
        Pair(
            listOf(listOf("1 teaspoon salt")),
            mapOf(" teaspoons salt" to 1.0 / 48.0)
        ),

        // A single uncommon ingredient should return an empty dict.
        Pair(
            listOf(listOf("1 pound meatloaf")),
            emptyMap<String, Double>()
        )
    )

    /**
     * Test that repeat common ingredients in a dict are correctly combined.
     *
     * Args:
     *     ingredientsDict: A map of the form
     *         {str representing ingredient to int representing amount}
     *         representing the expected ingredients and amounts, repeated
     *         common ingredients uncombined.
     *     dictionary: A map of the form
     *         {str representing ingredient to int representing amount}
     *         representing the expected ingredients and amounts, repeated
     *         common ingredients combined.
     */
    @Test
    fun testCombineSameIngredientsStandalone() {
        for ((ingredientsDict, dictionary) in
            combineSameIngredientsStandaloneCases) {

            val result: Map<String, Double> =
                combineSameIngredientsStandalone(ingredientsDict)

            assertEquals(dictionary, result)
        }
    }

    /**
     * Test that an ingredient list returns the correct corresponding dictionary.
     *
     * Args:
     *     listIngredientsPerAllRecipes: list of
     *         strings representing ingredients for each item in list of
     *         recipies.
     *     dictionary: A map of the form
     *         {str representing ingredient to int representing amount}
     *         representing the expected ingredients and amounts.
     */
    @Test
    fun testConvertToCups() {
        for ((listIngredientsPerAllRecipes, dictionary) in
            convertToCupsCases) {

            val result: Map<String, Double> =
                convertToCups(listIngredientsPerAllRecipes)

            assertEquals(dictionary, result)
        }
    }
}
