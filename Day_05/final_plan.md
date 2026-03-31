# Personalized Health & Fitness Plan

## Profile
{
  "age": 28,
  "weight_kg": 72,
  "height_cm": 175,
  "activity_level": "moderate",
  "diet_preference": "vegetarian",
  "fitness_goal": "fat loss"
}

## Meal Plan
{
  "daily_calories": 2135,
  "protein_g": 154,
  "carbs_g": 270,
  "fats_g": 56,
  "meals": [
    {
      "name": "Breakfast: High-Protein Berry Oatmeal",
      "description": "Start your day with a protein-packed and fiber-rich oatmeal. Combine 1/2 cup rolled oats cooked with water or unsweetened almond milk. Stir in 1.5 scoops of plant-based protein powder (e.g., pea or soy protein) for an extra protein boost. Top with 1 cup mixed berries and 1 tbsp chia seeds. This provides sustained energy and helps keep you full."
    },
    {
      "name": "Lunch: Quinoa & Chickpea Salad Bowl with Light Dressing",
      "description": "A vibrant and satisfying salad featuring 1 cup cooked quinoa and 1 cup cooked chickpeas as your base. Mix with 2 cups of fresh greens (spinach, lettuce), bell peppers, cucumber, and shredded carrots. Dress with 2 tablespoons of a light balsamic vinaigrette to keep fats in check. This meal is rich in complex carbohydrates, fiber, and plant-based protein."
    },
    {
      "name": "Snack 1: Edamame",
      "description": "A convenient and protein-dense snack. Enjoy 1.5 cups of shelled edamame, steamed or lightly boiled. Season with a pinch of sea salt. Edamame provides complete plant protein and healthy fats, making it an excellent choice for satiety."
    },
    {
      "name": "Dinner: Tempeh Stir-fry with Brown Rice",
      "description": "A flavorful and balanced dinner. Prepare a stir-fry with 150g tempeh, cubed, and 2 cups of mixed vegetables like broccoli, snow peas, and mushrooms. Saut\u00e9 with a minimal amount of 1 tsp sesame oil, soy sauce/tamari, fresh ginger, and garlic. Serve alongside 1 cup cooked brown rice. Tempeh is a fantastic source of fermented plant protein."
    },
    {
      "name": "Snack 2: Low-Fat Cottage Cheese with Fruit",
      "description": "A light, protein-rich snack. Enjoy 1 cup (225g) of low-fat cottage cheese (if lacto-ovo vegetarian) with 1/2 cup sliced peaches. If strictly vegan, opt for a small plant-based protein shake or a handful of almonds (adjusting macros accordingly)."
    }
  ]
}

## Workout Plan
{
  "warmup": [
    {
      "exercise": "Jumping Jacks",
      "duration_seconds": 60,
      "notes": "Begin with light cardio to gradually elevate your heart rate and warm up your muscles."
    },
    {
      "exercise": "High Knees",
      "duration_seconds": 30,
      "notes": "Bring your knees up towards your chest, maintaining a light jog."
    },
    {
      "exercise": "Butt Kicks",
      "duration_seconds": 30,
      "notes": "Kick your heels back towards your glutes, keeping the movement fluid."
    },
    {
      "exercise": "Arm Circles",
      "reps": "10 forward, 10 backward",
      "notes": "Perform large, controlled circles to warm up your shoulders and upper back."
    },
    {
      "exercise": "Torso Twists",
      "duration_seconds": 30,
      "notes": "Stand with feet shoulder-width apart and gently twist your torso from side to side, keeping your hips relatively stable."
    },
    {
      "exercise": "Leg Swings",
      "reps": "10 forward/backward, 10 side-to-side per leg",
      "notes": "Use a wall or chair for balance. Perform dynamic swings to open up your hips and hamstrings."
    }
  ],
  "main_workout": [
    {
      "type": "superset",
      "name": "Superset 1: Lower Body & Push Focus",
      "description": "Perform exercise 1A immediately followed by 1B with minimal rest. Rest after completing both exercises before starting the next set.",
      "sets": 4,
      "rest_between_sets_seconds": 60,
      "exercises": [
        {
          "exercise": "Goblet Squats",
          "reps": "12-15",
          "notes": "Hold a dumbbell vertically against your chest. If you don't have equipment, perform bodyweight squats, focusing on depth and form."
        },
        {
          "exercise": "Push-ups",
          "reps": "8-12",
          "notes": "Perform on your knees or toes, depending on your strength level. Keep your core engaged and body in a straight line from head to heels."
        }
      ]
    },
    {
      "type": "superset",
      "name": "Superset 2: Pull & Lower Body Focus",
      "description": "Perform exercise 2A immediately followed by 2B with minimal rest. Rest after completing both exercises before starting the next set.",
      "sets": 4,
      "rest_between_sets_seconds": 60,
      "exercises": [
        {
          "exercise": "Dumbbell Rows",
          "reps": "10-12 per arm",
          "notes": "Use a single dumbbell. Keep your back flat and core tight, pulling the dumbbell towards your hip. If no dumbbell, use a resistance band anchored under your feet."
        },
        {
          "exercise": "Walking Lunges",
          "reps": "10-12 per leg",
          "notes": "Step forward, lowering your hips until both knees are bent at approximately 90 degrees. Keep your torso upright. Hold light dumbbells for an added challenge."
        }
      ]
    },
    {
      "type": "circuit",
      "name": "Core & Stability Circuit",
      "description": "Perform all three exercises consecutively with minimal rest between them. Rest only after completing one full round.",
      "rounds": 3,
      "rest_between_rounds_seconds": 60,
      "exercises": [
        {
          "exercise": "Plank",
          "hold_seconds": 45,
          "notes": "Maintain a straight line from your head to your heels, engaging your core and glutes."
        },
        {
          "exercise": "Russian Twists",
          "reps": "15-20 per side",
          "notes": "Sit with your knees bent and feet off the floor (optional), lean back slightly. Twist your torso, touching your hands to the floor on each side. Hold a light weight for more intensity."
        },
        {
          "exercise": "Bird-Dog",
          "reps": "10 per side",
          "notes": "Start on all fours. Extend your opposite arm and leg simultaneously, keeping your core stable and back flat. Focus on control, not speed."
        }
      ]
    },
    {
      "type": "finisher",
      "name": "Cardio Finisher",
      "description": "Perform these two exercises back-to-back with no rest. Rest after both, then repeat for the total number of rounds.",
      "rounds": 3,
      "rest_between_rounds_seconds": 60,
      "exercises": [
        {
          "exercise": "High Knees",
          "duration_seconds": 30,
          "notes": "Explode with high knees, driving them towards your chest as quickly as possible."
        },
        {
          "exercise": "Burpees",
          "duration_seconds": 30,
          "notes": "Perform full burpees with a push-up and jump, or modify by stepping back and omitting the push-up/jump."
        }
      ]
    }
  ],
  "cooldown": [
    {
      "stretch": "Standing Quad Stretch",
      "hold_seconds": 30,
      "side": "each leg",
      "notes": "Stand tall, grab your ankle, and gently pull your heel towards your glutes. Keep your knees together."
    },
    {
      "stretch": "Hamstring Stretch (Seated or Standing)",
      "hold_seconds": 30,
      "side": "each leg",
      "notes": "From a seated position, extend one leg and reach for your toes, or stand and place your heel on an elevated surface, leaning forward from your hips."
    },
    {
      "stretch": "Triceps Stretch",
      "hold_seconds": 30,
      "side": "each arm",
      "notes": "Reach one arm overhead, bend your elbow, and use your other hand to gently push the elbow down."
    },
    {
      "stretch": "Chest Stretch",
      "hold_seconds": 30,
      "notes": "Clasp your hands behind your back and gently lift them, or use a doorway by placing your forearm on the frame and gently leaning forward."
    },
    {
      "stretch": "Cobra Stretch",
      "hold_seconds": 30,
      "notes": "Lie on your stomach, place your hands under your shoulders, and gently push up, keeping your hips on the floor for a gentle back extension."
    },
    {
      "stretch": "Child's Pose",
      "hold_seconds": 60,
      "notes": "Kneel on the floor, sit back on your heels, and fold your torso forward, extending your arms forward or resting them by your sides. Relax and breathe deeply."
    }
  ],
  "duration_minutes": 60
}

## Weekly Strategy
{
  "weekly_schedule": [
    {
      "day": "Monday",
      "focus": "Full Body Strength & Cardio Kickoff",
      "meal_plan": [
        {
          "name": "Breakfast: High-Protein Berry Oatmeal",
          "description": "Start your day with a protein-packed and fiber-rich oatmeal. Combine 1/2 cup rolled oats cooked with water or unsweetened almond milk. Stir in 1.5 scoops of plant-based protein powder (e.g., pea or soy protein) for an extra protein boost. Top with 1 cup mixed berries and 1 tbsp chia seeds. This provides sustained energy and helps keep you full."
        },
        {
          "name": "Lunch: Quinoa & Chickpea Salad Bowl with Light Dressing",
          "description": "A vibrant and satisfying salad featuring 1 cup cooked quinoa and 1 cup cooked chickpeas as your base. Mix with 2 cups of fresh greens (spinach, lettuce), bell peppers, cucumber, and shredded carrots. Dress with 2 tablespoons of a light balsamic vinaigrette to keep fats in check. This meal is rich in complex carbohydrates, fiber, and plant-based protein."
        },
        {
          "name": "Snack 1: Edamame",
          "description": "A convenient and protein-dense snack. Enjoy 1.5 cups of shelled edamame, steamed or lightly boiled. Season with a pinch of sea salt. Edamame provides complete plant protein and healthy fats, making it an excellent choice for satiety."
        },
        {
          "name": "Dinner: Tempeh Stir-fry with Brown Rice",
          "description": "A flavorful and balanced dinner. Prepare a stir-fry with 150g tempeh, cubed, and 2 cups of mixed vegetables like broccoli, snow peas, and mushrooms. Saut\u00e9 with a minimal amount of 1 tsp sesame oil, soy sauce/tamari, fresh ginger, and garlic. Serve alongside 1 cup cooked brown rice. Tempeh is a fantastic source of fermented plant protein."
        },
        {
          "name": "Snack 2: Low-Fat Cottage Cheese with Fruit",
          "description": "A light, protein-rich snack. Enjoy 1 cup (225g) of low-fat cottage cheese (if lacto-ovo vegetarian) with 1/2 cup sliced peaches. If strictly vegan, opt for a small plant-based protein shake or a handful of almonds (adjusting macros accordingly)."
        }
      ],
      "workout_plan": {
        "warmup": [
          {
            "exercise": "Jumping Jacks",
            "duration_seconds": 60,
            "notes": "Begin with light cardio to gradually elevate your heart rate and warm up your muscles."
          },
          {
            "exercise": "High Knees",
            "duration_seconds": 30,
            "notes": "Bring your knees up towards your chest, maintaining a light jog."
          },
          {
            "exercise": "Butt Kicks",
            "duration_seconds": 30,
            "notes": "Kick your heels back towards your glutes, keeping the movement fluid."
          },
          {
            "exercise": "Arm Circles",
            "reps": "10 forward, 10 backward",
            "notes": "Perform large, controlled circles to warm up your shoulders and upper back."
          },
          {
            "exercise": "Torso Twists",
            "duration_seconds": 30,
            "notes": "Stand with feet shoulder-width apart and gently twist your torso from side to side, keeping your hips relatively stable."
          },
          {
            "exercise": "Leg Swings",
            "reps": "10 forward/backward, 10 side-to-side per leg",
            "notes": "Use a wall or chair for balance. Perform dynamic swings to open up your hips and hamstrings."
          }
        ],
        "main_workout": [
          {
            "type": "superset",
            "name": "Superset 1: Lower Body & Push Focus",
            "description": "Perform exercise 1A immediately followed by 1B with minimal rest. Rest after completing both exercises before starting the next set.",
            "sets": 4,
            "rest_between_sets_seconds": 60,
            "exercises": [
              {
                "exercise": "Goblet Squats",
                "reps": "12-15",
                "notes": "Hold a dumbbell vertically against your chest. If you don't have equipment, perform bodyweight squats, focusing on depth and form."
              },
              {
                "exercise": "Push-ups",
                "reps": "8-12",
                "notes": "Perform on your knees or toes, depending on your strength level. Keep your core engaged and body in a straight line from head to heels."
              }
            ]
          },
          {
            "type": "superset",
            "name": "Superset 2: Pull & Lower Body Focus",
            "description": "Perform exercise 2A immediately followed by 2B with minimal rest. Rest after completing both exercises before starting the next set.",
            "sets": 4,
            "rest_between_sets_seconds": 60,
            "exercises": [
              {
                "exercise": "Dumbbell Rows",
                "reps": "10-12 per arm",
                "notes": "Use a single dumbbell. Keep your back flat and core tight, pulling the dumbbell towards your hip. If no dumbbell, use a resistance band anchored under your feet."
              },
              {
                "exercise": "Walking Lunges",
                "reps": "10-12 per leg",
                "notes": "Step forward, lowering your hips until both knees are bent at approximately 90 degrees. Keep your torso upright. Hold light dumbbells for an added challenge."
              }
            ]
          },
          {
            "type": "circuit",
            "name": "Core & Stability Circuit",
            "description": "Perform all three exercises consecutively with minimal rest between them. Rest only after completing one full round.",
            "rounds": 3,
            "rest_between_rounds_seconds": 60,
            "exercises": [
              {
                "exercise": "Plank",
                "hold_seconds": 45,
                "notes": "Maintain a straight line from your head to your heels, engaging your core and glutes."
              },
              {
                "exercise": "Russian Twists",
                "reps": "15-20 per side",
                "notes": "Sit with your knees bent and feet off the floor (optional), lean back slightly. Twist your torso, touching your hands to the floor on each side. Hold a light weight for more intensity."
              },
              {
                "exercise": "Bird-Dog",
                "reps": "10 per side",
                "notes": "Start on all fours. Extend your opposite arm and leg simultaneously, keeping your core stable and back flat. Focus on control, not speed."
              }
            ]
          },
          {
            "type": "finisher",
            "name": "Cardio Finisher",
            "description": "Perform these two exercises back-to-back with no rest. Rest after both, then repeat for the total number of rounds.",
            "rounds": 3,
            "rest_between_rounds_seconds": 60,
            "exercises": [
              {
                "exercise": "High Knees",
                "duration_seconds": 30,
                "notes": "Explode with high knees, driving them towards your chest as quickly as possible."
              },
              {
                "exercise": "Burpees",
                "duration_seconds": 30,
                "notes": "Perform full burpees with a push-up and jump, or modify by stepping back and omitting the push-up/jump."
              }
            ]
          }
        ],
        "cooldown": [
          {
            "stretch": "Standing Quad Stretch",
            "hold_seconds": 30,
            "side": "each leg",
            "notes": "Stand tall, grab your ankle, and gently pull your heel towards your glutes. Keep your knees together."
          },
          {
            "stretch": "Hamstring Stretch (Seated or Standing)",
            "hold_seconds": 30,
            "side": "each leg",
            "notes": "From a seated position, extend one leg and reach for your toes, or stand and place your heel on an elevated surface, leaning forward from your hips."
          },
          {
            "stretch": "Triceps Stretch",
            "hold_seconds": 30,
            "side": "each arm",
            "notes": "Reach one arm overhead, bend your elbow, and use your other hand to gently push the elbow down."
          },
          {
            "stretch": "Chest Stretch",
            "hold_seconds": 30,
            "notes": "Clasp your hands behind your back and gently lift them, or use a doorway by placing your forearm on the frame and gently leaning forward."
          },
          {
            "stretch": "Cobra Stretch",
            "hold_seconds": 30,
            "notes": "Lie on your stomach, place your hands under your shoulders, and gently push up, keeping your hips on the floor for a gentle back extension."
          },
          {
            "stretch": "Child's Pose",
            "hold_seconds": 60,
            "notes": "Kneel on the floor, sit back on your heels, and fold your torso forward, extending your arms forward or resting them by your sides. Relax and breathe deeply."
          }
        ],
        "duration_minutes": 60
      },
      "notes": "Start your week strong! Have your high-protein berry oatmeal about 60-90 minutes before your workout to fuel your session. Follow up with your first snack or lunch soon after to support muscle recovery and growth. Focus on excellent form."
    },
    {
      "day": "Tuesday",
      "focus": "Active Recovery & Hydration",
      "meal_plan": [
        {
          "name": "Breakfast: High-Protein Berry Oatmeal",
          "description": "Start your day with a protein-packed and fiber-rich oatmeal. Combine 1/2 cup rolled oats cooked with water or unsweetened almond milk. Stir in 1.5 scoops of plant-based protein powder (e.g., pea or soy protein) for an extra protein boost. Top with 1 cup mixed berries and 1 tbsp chia seeds. This provides sustained energy and helps keep you full."
        },
        {
          "name": "Lunch: Quinoa & Chickpea Salad Bowl with Light Dressing",
          "description": "A vibrant and satisfying salad featuring 1 cup cooked quinoa and 1 cup cooked chickpeas as your base. Mix with 2 cups of fresh greens (spinach, lettuce), bell peppers, cucumber, and shredded carrots. Dress with 2 tablespoons of a light balsamic vinaigrette to keep fats in check. This meal is rich in complex carbohydrates, fiber, and plant-based protein."
        },
        {
          "name": "Snack 1: Edamame",
          "description": "A convenient and protein-dense snack. Enjoy 1.5 cups of shelled edamame, steamed or lightly boiled. Season with a pinch of sea salt. Edamame provides complete plant protein and healthy fats, making it an excellent choice for satiety."
        },
        {
          "name": "Dinner: Tempeh Stir-fry with Brown Rice",
          "description": "A flavorful and balanced dinner. Prepare a stir-fry with 150g tempeh, cubed, and 2 cups of mixed vegetables like broccoli, snow peas, and mushrooms. Saut\u00e9 with a minimal amount of 1 tsp sesame oil, soy sauce/tamari, fresh ginger, and garlic. Serve alongside 1 cup cooked brown rice. Tempeh is a fantastic source of fermented plant protein."
        },
        {
          "name": "Snack 2: Low-Fat Cottage Cheese with Fruit",
          "description": "A light, protein-rich snack. Enjoy 1 cup (225g) of low-fat cottage cheese (if lacto-ovo vegetarian) with 1/2 cup sliced peaches. If strictly vegan, opt for a small plant-based protein shake or a handful of almonds (adjusting macros accordingly)."
        }
      ],
      "workout_plan": null,
      "notes": "Today is for active recovery. Consider a brisk 30-minute walk, light stretching, or a gentle yoga session to promote blood flow and aid muscle repair. Focus intently on your hydration and nourishing your body with balanced meals."
    },
    {
      "day": "Wednesday",
      "focus": "Full Body Strength & Cardio Push",
      "meal_plan": [
        {
          "name": "Breakfast: High-Protein Berry Oatmeal",
          "description": "Start your day with a protein-packed and fiber-rich oatmeal. Combine 1/2 cup rolled oats cooked with water or unsweetened almond milk. Stir in 1.5 scoops of plant-based protein powder (e.g., pea or soy protein) for an extra protein boost. Top with 1 cup mixed berries and 1 tbsp chia seeds. This provides sustained energy and helps keep you full."
        },
        {
          "name": "Lunch: Quinoa & Chickpea Salad Bowl with Light Dressing",
          "description": "A vibrant and satisfying salad featuring 1 cup cooked quinoa and 1 cup cooked chickpeas as your base. Mix with 2 cups of fresh greens (spinach, lettuce), bell peppers, cucumber, and shredded carrots. Dress with 2 tablespoons of a light balsamic vinaigrette to keep fats in check. This meal is rich in complex carbohydrates, fiber, and plant-based protein."
        },
        {
          "name": "Snack 1: Edamame",
          "description": "A convenient and protein-dense snack. Enjoy 1.5 cups of shelled edamame, steamed or lightly boiled. Season with a pinch of sea salt. Edamame provides complete plant protein and healthy fats, making it an excellent choice for satiety."
        },
        {
          "name": "Dinner: Tempeh Stir-fry with Brown Rice",
          "description": "A flavorful and balanced dinner. Prepare a stir-fry with 150g tempeh, cubed, and 2 cups of mixed vegetables like broccoli, snow peas, and mushrooms. Saut\u00e9 with a minimal amount of 1 tsp sesame oil, soy sauce/tamari, fresh ginger, and garlic. Serve alongside 1 cup cooked brown rice. Tempeh is a fantastic source of fermented plant protein."
        },
        {
          "name": "Snack 2: Low-Fat Cottage Cheese with Fruit",
          "description": "A light, protein-rich snack. Enjoy 1 cup (225g) of low-fat cottage cheese (if lacto-ovo vegetarian) with 1/2 cup sliced peaches. If strictly vegan, opt for a small plant-based protein shake or a handful of almonds (adjusting macros accordingly)."
        }
      ],
      "workout_plan": {
        "warmup": [
          {
            "exercise": "Jumping Jacks",
            "duration_seconds": 60,
            "notes": "Begin with light cardio to gradually elevate your heart rate and warm up your muscles."
          },
          {
            "exercise": "High Knees",
            "duration_seconds": 30,
            "notes": "Bring your knees up towards your chest, maintaining a light jog."
          },
          {
            "exercise": "Butt Kicks",
            "duration_seconds": 30,
            "notes": "Kick your heels back towards your glutes, keeping the movement fluid."
          },
          {
            "exercise": "Arm Circles",
            "reps": "10 forward, 10 backward",
            "notes": "Perform large, controlled circles to warm up your shoulders and upper back."
          },
          {
            "exercise": "Torso Twists",
            "duration_seconds": 30,
            "notes": "Stand with feet shoulder-width apart and gently twist your torso from side to side, keeping your hips relatively stable."
          },
          {
            "exercise": "Leg Swings",
            "reps": "10 forward/backward, 10 side-to-side per leg",
            "notes": "Use a wall or chair for balance. Perform dynamic swings to open up your hips and hamstrings."
          }
        ],
        "main_workout": [
          {
            "type": "superset",
            "name": "Superset 1: Lower Body & Push Focus",
            "description": "Perform exercise 1A immediately followed by 1B with minimal rest. Rest after completing both exercises before starting the next set.",
            "sets": 4,
            "rest_between_sets_seconds": 60,
            "exercises": [
              {
                "exercise": "Goblet Squats",
                "reps": "12-15",
                "notes": "Hold a dumbbell vertically against your chest. If you don't have equipment, perform bodyweight squats, focusing on depth and form."
              },
              {
                "exercise": "Push-ups",
                "reps": "8-12",
                "notes": "Perform on your knees or toes, depending on your strength level. Keep your core engaged and body in a straight line from head to heels."
              }
            ]
          },
          {
            "type": "superset",
            "name": "Superset 2: Pull & Lower Body Focus",
            "description": "Perform exercise 2A immediately followed by 2B with minimal rest. Rest after completing both exercises before starting the next set.",
            "sets": 4,
            "rest_between_sets_seconds": 60,
            "exercises": [
              {
                "exercise": "Dumbbell Rows",
                "reps": "10-12 per arm",
                "notes": "Use a single dumbbell. Keep your back flat and core tight, pulling the dumbbell towards your hip. If no dumbbell, use a resistance band anchored under your feet."
              },
              {
                "exercise": "Walking Lunges",
                "reps": "10-12 per leg",
                "notes": "Step forward, lowering your hips until both knees are bent at approximately 90 degrees. Keep your torso upright. Hold light dumbbells for an added challenge."
              }
            ]
          },
          {
            "type": "circuit",
            "name": "Core & Stability Circuit",
            "description": "Perform all three exercises consecutively with minimal rest between them. Rest only after completing one full round.",
            "rounds": 3,
            "rest_between_rounds_seconds": 60,
            "exercises": [
              {
                "exercise": "Plank",
                "hold_seconds": 45,
                "notes": "Maintain a straight line from your head to your heels, engaging your core and glutes."
              },
              {
                "exercise": "Russian Twists",
                "reps": "15-20 per side",
                "notes": "Sit with your knees bent and feet off the floor (optional), lean back slightly. Twist your torso, touching your hands to the floor on each side. Hold a light weight for more intensity."
              },
              {
                "exercise": "Bird-Dog",
                "reps": "10 per side",
                "notes": "Start on all fours. Extend your opposite arm and leg simultaneously, keeping your core stable and back flat. Focus on control, not speed."
              }
            ]
          },
          {
            "type": "finisher",
            "name": "Cardio Finisher",
            "description": "Perform these two exercises back-to-back with no rest. Rest after both, then repeat for the total number of rounds.",
            "rounds": 3,
            "rest_between_rounds_seconds": 60,
            "exercises": [
              {
                "exercise": "High Knees",
                "duration_seconds": 30,
                "notes": "Explode with high knees, driving them towards your chest as quickly as possible."
              },
              {
                "exercise": "Burpees",
                "duration_seconds": 30,
                "notes": "Perform full burpees with a push-up and jump, or modify by stepping back and omitting the push-up/jump."
              }
            ]
          }
        ],
        "cooldown": [
          {
            "stretch": "Standing Quad Stretch",
            "hold_seconds": 30,
            "side": "each leg",
            "notes": "Stand tall, grab your ankle, and gently pull your heel towards your glutes. Keep your knees together."
          },
          {
            "stretch": "Hamstring Stretch (Seated or Standing)",
            "hold_seconds": 30,
            "side": "each leg",
            "notes": "From a seated position, extend one leg and reach for your toes, or stand and place your heel on an elevated surface, leaning forward from your hips."
          },
          {
            "stretch": "Triceps Stretch",
            "hold_seconds": 30,
            "side": "each arm",
            "notes": "Reach one arm overhead, bend your elbow, and use your other hand to gently push the elbow down."
          },
          {
            "stretch": "Chest Stretch",
            "hold_seconds": 30,
            "notes": "Clasp your hands behind your back and gently lift them, or use a doorway by placing your forearm on the frame and gently leaning forward."
          },
          {
            "stretch": "Cobra Stretch",
            "hold_seconds": 30,
            "notes": "Lie on your stomach, place your hands under your shoulders, and gently push up, keeping your hips on the floor for a gentle back extension."
          },
          {
            "stretch": "Child's Pose",
            "hold_seconds": 60,
            "notes": "Kneel on the floor, sit back on your heels, and fold your torso forward, extending your arms forward or resting them by your sides. Relax and breathe deeply."
          }
        ],
        "duration_minutes": 60
      },
      "notes": "You're halfway through your workout week! Remember to listen to your body. If you're feeling strong, aim for the higher end of the rep range or slightly increase your intensity. If you're a bit fatigued, it's okay to ease up. Protein intake is vital today for muscle repair."
    },
    {
      "day": "Thursday",
      "focus": "Rest & Mental Recharge",
      "meal_plan": [
        {
          "name": "Breakfast: High-Protein Berry Oatmeal",
          "description": "Start your day with a protein-packed and fiber-rich oatmeal. Combine 1/2 cup rolled oats cooked with water or unsweetened almond milk. Stir in 1.5 scoops of plant-based protein powder (e.g., pea or soy protein) for an extra protein boost. Top with 1 cup mixed berries and 1 tbsp chia seeds. This provides sustained energy and helps keep you full."
        },
        {
          "name": "Lunch: Quinoa & Chickpea Salad Bowl with Light Dressing",
          "description": "A vibrant and satisfying salad featuring 1 cup cooked quinoa and 1 cup cooked chickpeas as your base. Mix with 2 cups of fresh greens (spinach, lettuce), bell peppers, cucumber, and shredded carrots. Dress with 2 tablespoons of a light balsamic vinaigrette to keep fats in check. This meal is rich in complex carbohydrates, fiber, and plant-based protein."
        },
        {
          "name": "Snack 1: Edamame",
          "description": "A convenient and protein-dense snack. Enjoy 1.5 cups of shelled edamame, steamed or lightly boiled. Season with a pinch of sea salt. Edamame provides complete plant protein and healthy fats, making it an excellent choice for satiety."
        },
        {
          "name": "Dinner: Tempeh Stir-fry with Brown Rice",
          "description": "A flavorful and balanced dinner. Prepare a stir-fry with 150g tempeh, cubed, and 2 cups of mixed vegetables like broccoli, snow peas, and mushrooms. Saut\u00e9 with a minimal amount of 1 tsp sesame oil, soy sauce/tamari, fresh ginger, and garlic. Serve alongside 1 cup cooked brown rice. Tempeh is a fantastic source of fermented plant protein."
        },
        {
          "name": "Snack 2: Low-Fat Cottage Cheese with Fruit",
          "description": "A light, protein-rich snack. Enjoy 1 cup (225g) of low-fat cottage cheese (if lacto-ovo vegetarian) with 1/2 cup sliced peaches. If strictly vegan, opt for a small plant-based protein shake or a handful of almonds (adjusting macros accordingly)."
        }
      ],
      "workout_plan": null,
      "notes": "Embrace this rest day fully! Your body recovers and builds strength when you rest. Focus on mindful eating, staying hydrated, and prioritizing a good night's sleep. This is also a great day to do some meal prep for the upcoming weekend."
    },
    {
      "day": "Friday",
      "focus": "Full Body Strength & Cardio - Week's Finale",
      "meal_plan": [
        {
          "name": "Breakfast: High-Protein Berry Oatmeal",
          "description": "Start your day with a protein-packed and fiber-rich oatmeal. Combine 1/2 cup rolled oats cooked with water or unsweetened almond milk. Stir in 1.5 scoops of plant-based protein powder (e.g., pea or soy protein) for an extra protein boost. Top with 1 cup mixed berries and 1 tbsp chia seeds. This provides sustained energy and helps keep you full."
        },
        {
          "name": "Lunch: Quinoa & Chickpea Salad Bowl with Light Dressing",
          "description": "A vibrant and satisfying salad featuring 1 cup cooked quinoa and 1 cup cooked chickpeas as your base. Mix with 2 cups of fresh greens (spinach, lettuce), bell peppers, cucumber, and shredded carrots. Dress with 2 tablespoons of a light balsamic vinaigrette to keep fats in check. This meal is rich in complex carbohydrates, fiber, and plant-based protein."
        },
        {
          "name": "Snack 1: Edamame",
          "description": "A convenient and protein-dense snack. Enjoy 1.5 cups of shelled edamame, steamed or lightly boiled. Season with a pinch of sea salt. Edamame provides complete plant protein and healthy fats, making it an excellent choice for satiety."
        },
        {
          "name": "Dinner: Tempeh Stir-fry with Brown Rice",
          "description": "A flavorful and balanced dinner. Prepare a stir-fry with 150g tempeh, cubed, and 2 cups of mixed vegetables like broccoli, snow peas, and mushrooms. Saut\u00e9 with a minimal amount of 1 tsp sesame oil, soy sauce/tamari, fresh ginger, and garlic. Serve alongside 1 cup cooked brown rice. Tempeh is a fantastic source of fermented plant protein."
        },
        {
          "name": "Snack 2: Low-Fat Cottage Cheese with Fruit",
          "description": "A light, protein-rich snack. Enjoy 1 cup (225g) of low-fat cottage cheese (if lacto-ovo vegetarian) with 1/2 cup sliced peaches. If strictly vegan, opt for a small plant-based protein shake or a handful of almonds (adjusting macros accordingly)."
        }
      ],
      "workout_plan": {
        "warmup": [
          {
            "exercise": "Jumping Jacks",
            "duration_seconds": 60,
            "notes": "Begin with light cardio to gradually elevate your heart rate and warm up your muscles."
          },
          {
            "exercise": "High Knees",
            "duration_seconds": 30,
            "notes": "Bring your knees up towards your chest, maintaining a light jog."
          },
          {
            "exercise": "Butt Kicks",
            "duration_seconds": 30,
            "notes": "Kick your heels back towards your glutes, keeping the movement fluid."
          },
          {
            "exercise": "Arm Circles",
            "reps": "10 forward, 10 backward",
            "notes": "Perform large, controlled circles to warm up your shoulders and upper back."
          },
          {
            "exercise": "Torso Twists",
            "duration_seconds": 30,
            "notes": "Stand with feet shoulder-width apart and gently twist your torso from side to side, keeping your hips relatively stable."
          },
          {
            "exercise": "Leg Swings",
            "reps": "10 forward/backward, 10 side-to-side per leg",
            "notes": "Use a wall or chair for balance. Perform dynamic swings to open up your hips and hamstrings."
          }
        ],
        "main_workout": [
          {
            "type": "superset",
            "name": "Superset 1: Lower Body & Push Focus",
            "description": "Perform exercise 1A immediately followed by 1B with minimal rest. Rest after completing both exercises before starting the next set.",
            "sets": 4,
            "rest_between_sets_seconds": 60,
            "exercises": [
              {
                "exercise": "Goblet Squats",
                "reps": "12-15",
                "notes": "Hold a dumbbell vertically against your chest. If you don't have equipment, perform bodyweight squats, focusing on depth and form."
              },
              {
                "exercise": "Push-ups",
                "reps": "8-12",
                "notes": "Perform on your knees or toes, depending on your strength level. Keep your core engaged and body in a straight line from head to heels."
              }
            ]
          },
          {
            "type": "superset",
            "name": "Superset 2: Pull & Lower Body Focus",
            "description": "Perform exercise 2A immediately followed by 2B with minimal rest. Rest after completing both exercises before starting the next set.",
            "sets": 4,
            "rest_between_sets_seconds": 60,
            "exercises": [
              {
                "exercise": "Dumbbell Rows",
                "reps": "10-12 per arm",
                "notes": "Use a single dumbbell. Keep your back flat and core tight, pulling the dumbbell towards your hip. If no dumbbell, use a resistance band anchored under your feet."
              },
              {
                "exercise": "Walking Lunges",
                "reps": "10-12 per leg",
                "notes": "Step forward, lowering your hips until both knees are bent at approximately 90 degrees. Keep your torso upright. Hold light dumbbells for an added challenge."
              }
            ]
          },
          {
            "type": "circuit",
            "name": "Core & Stability Circuit",
            "description": "Perform all three exercises consecutively with minimal rest between them. Rest only after completing one full round.",
            "rounds": 3,
            "rest_between_rounds_seconds": 60,
            "exercises": [
              {
                "exercise": "Plank",
                "hold_seconds": 45,
                "notes": "Maintain a straight line from your head to your heels, engaging your core and glutes."
              },
              {
                "exercise": "Russian Twists",
                "reps": "15-20 per side",
                "notes": "Sit with your knees bent and feet off the floor (optional), lean back slightly. Twist your torso, touching your hands to the floor on each side. Hold a light weight for more intensity."
              },
              {
                "exercise": "Bird-Dog",
                "reps": "10 per side",
                "notes": "Start on all fours. Extend your opposite arm and leg simultaneously, keeping your core stable and back flat. Focus on control, not speed."
              }
            ]
          },
          {
            "type": "finisher",
            "name": "Cardio Finisher",
            "description": "Perform these two exercises back-to-back with no rest. Rest after both, then repeat for the total number of rounds.",
            "rounds": 3,
            "rest_between_rounds_seconds": 60,
            "exercises": [
              {
                "exercise": "High Knees",
                "duration_seconds": 30,
                "notes": "Explode with high knees, driving them towards your chest as quickly as possible."
              },
              {
                "exercise": "Burpees",
                "duration_seconds": 30,
                "notes": "Perform full burpees with a push-up and jump, or modify by stepping back and omitting the push-up/jump."
              }
            ]
          }
        ],
        "cooldown": [
          {
            "stretch": "Standing Quad Stretch",
            "hold_seconds": 30,
            "side": "each leg",
            "notes": "Stand tall, grab your ankle, and gently pull your heel towards your glutes. Keep your knees together."
          },
          {
            "stretch": "Hamstring Stretch (Seated or Standing)",
            "hold_seconds": 30,
            "side": "each leg",
            "notes": "From a seated position, extend one leg and reach for your toes, or stand and place your heel on an elevated surface, leaning forward from your hips."
          },
          {
            "stretch": "Triceps Stretch",
            "hold_seconds": 30,
            "side": "each arm",
            "notes": "Reach one arm overhead, bend your elbow, and use your other hand to gently push the elbow down."
          },
          {
            "stretch": "Chest Stretch",
            "hold_seconds": 30,
            "notes": "Clasp your hands behind your back and gently lift them, or use a doorway by placing your forearm on the frame and gently leaning forward."
          },
          {
            "stretch": "Cobra Stretch",
            "hold_seconds": 30,
            "notes": "Lie on your stomach, place your hands under your shoulders, and gently push up, keeping your hips on the floor for a gentle back extension."
          },
          {
            "stretch": "Child's Pose",
            "hold_seconds": 60,
            "notes": "Kneel on the floor, sit back on your heels, and fold your torso forward, extending your arms forward or resting them by your sides. Relax and breathe deeply."
          }
        ],
        "duration_minutes": 60
      },
      "notes": "You've made it to your last strength session of the week! Give it your all, maintaining focus on proper execution. Celebrate your consistency with a delicious and nutritious dinner, and prepare for a well-deserved restful weekend."
    },
    {
      "day": "Saturday",
      "focus": "Active Lifestyle & Enjoyment",
      "meal_plan": [
        {
          "name": "Breakfast: High-Protein Berry Oatmeal",
          "description": "Start your day with a protein-packed and fiber-rich oatmeal. Combine 1/2 cup rolled oats cooked with water or unsweetened almond milk. Stir in 1.5 scoops of plant-based protein powder (e.g., pea or soy protein) for an extra protein boost. Top with 1 cup mixed berries and 1 tbsp chia seeds. This provides sustained energy and helps keep you full."
        },
        {
          "name": "Lunch: Quinoa & Chickpea Salad Bowl with Light Dressing",
          "description": "A vibrant and satisfying salad featuring 1 cup cooked quinoa and 1 cup cooked chickpeas as your base. Mix with 2 cups of fresh greens (spinach, lettuce), bell peppers, cucumber, and shredded carrots. Dress with 2 tablespoons of a light balsamic vinaigrette to keep fats in check. This meal is rich in complex carbohydrates, fiber, and plant-based protein."
        },
        {
          "name": "Snack 1: Edamame",
          "description": "A convenient and protein-dense snack. Enjoy 1.5 cups of shelled edamame, steamed or lightly boiled. Season with a pinch of sea salt. Edamame provides complete plant protein and healthy fats, making it an excellent choice for satiety."
        },
        {
          "name": "Dinner: Tempeh Stir-fry with Brown Rice",
          "description": "A flavorful and balanced dinner. Prepare a stir-fry with 150g tempeh, cubed, and 2 cups of mixed vegetables like broccoli, snow peas, and mushrooms. Saut\u00e9 with a minimal amount of 1 tsp sesame oil, soy sauce/tamari, fresh ginger, and garlic. Serve alongside 1 cup cooked brown rice. Tempeh is a fantastic source of fermented plant protein."
        },
        {
          "name": "Snack 2: Low-Fat Cottage Cheese with Fruit",
          "description": "A light, protein-rich snack. Enjoy 1 cup (225g) of low-fat cottage cheese (if lacto-ovo vegetarian) with 1/2 cup sliced peaches. If strictly vegan, opt for a small plant-based protein shake or a handful of almonds (adjusting macros accordingly)."
        }
      ],
      "workout_plan": null,
      "notes": "Embrace the weekend! Engage in activities you enjoy that keep you moving, like a long walk, cycling, hiking, or playing a casual sport. Keep your meals balanced and continue to prioritize hydration."
    },
    {
      "day": "Sunday",
      "focus": "Full Rest & Weekly Preparation",
      "meal_plan": [
        {
          "name": "Breakfast: High-Protein Berry Oatmeal",
          "description": "Start your day with a protein-packed and fiber-rich oatmeal. Combine 1/2 cup rolled oats cooked with water or unsweetened almond milk. Stir in 1.5 scoops of plant-based protein powder (e.g., pea or soy protein) for an extra protein boost. Top with 1 cup mixed berries and 1 tbsp chia seeds. This provides sustained energy and helps keep you full."
        },
        {
          "name": "Lunch: Quinoa & Chickpea Salad Bowl with Light Dressing",
          "description": "A vibrant and satisfying salad featuring 1 cup cooked quinoa and 1 cup cooked chickpeas as your base. Mix with 2 cups of fresh greens (spinach, lettuce), bell peppers, cucumber, and shredded carrots. Dress with 2 tablespoons of a light balsamic vinaigrette to keep fats in check. This meal is rich in complex carbohydrates, fiber, and plant-based protein."
        },
        {
          "name": "Snack 1: Edamame",
          "description": "A convenient and protein-dense snack. Enjoy 1.5 cups of shelled edamame, steamed or lightly boiled. Season with a pinch of sea salt. Edamame provides complete plant protein and healthy fats, making it an excellent choice for satiety."
        },
        {
          "name": "Dinner: Tempeh Stir-fry with Brown Rice",
          "description": "A flavorful and balanced dinner. Prepare a stir-fry with 150g tempeh, cubed, and 2 cups of mixed vegetables like broccoli, snow peas, and mushrooms. Saut\u00e9 with a minimal amount of 1 tsp sesame oil, soy sauce/tamari, fresh ginger, and garlic. Serve alongside 1 cup cooked brown rice. Tempeh is a fantastic source of fermented plant protein."
        },
        {
          "name": "Snack 2: Low-Fat Cottage Cheese with Fruit",
          "description": "A light, protein-rich snack. Enjoy 1 cup (225g) of low-fat cottage cheese (if lacto-ovo vegetarian) with 1/2 cup sliced peaches. If strictly vegan, opt for a small plant-based protein shake or a handful of almonds (adjusting macros accordingly)."
        }
      ],
      "workout_plan": null,
      "notes": "A day for complete physical and mental rest. Use this time to prepare for the week ahead \u2013 plan your meals, organize your gym bag, and set your intentions for another successful week of health and fitness. Get ready to crush it again!"
    }
  ],
  "tips": [
    {
      "title": "Hydration is Key",
      "description": "Drink plenty of water throughout the day, especially before, during, and after your workouts. Aim for at least 8-10 glasses to support metabolism, energy, and recovery."
    },
    {
      "title": "Listen to Your Body",
      "description": "It's important to challenge yourself, but also to recognize when your body needs rest. Don't be afraid to take an extra rest day or modify an exercise if you're feeling overly fatigued or experience pain. Recovery is just as important as training!"
    },
    {
      "title": "Prioritize Sleep",
      "description": "Aim for 7-9 hours of quality sleep each night. Sleep is crucial for muscle repair, hormone regulation, energy levels, and overall well-being. It's when your body truly rebuilds."
    },
    {
      "title": "Meal Prepping for Success",
      "description": "Prepare your meals and snacks in advance, especially on your rest days. This significantly helps ensure you stick to your nutritional goals, saves time during busy weekdays, and reduces the temptation for less healthy options."
    },
    {
      "title": "Focus on Form",
      "description": "Always prioritize proper form over lifting heavier weights or doing more reps. Good form prevents injury, ensures you're effectively targeting the right muscles, and maximizes the benefits of each exercise. Watch videos or use a mirror to check your technique."
    },
    {
      "title": "Consistency Over Perfection",
      "description": "Don't get discouraged by occasional slip-ups or missed workouts. Consistency in both your diet and exercise is what truly leads to long-term results. Get back on track with your next meal or workout; progress isn't linear, but persistent effort pays off."
    },
    {
      "title": "Adjust as Needed",
      "description": "This plan is a guideline. Feel free to adjust portion sizes slightly based on your hunger and energy levels, or swap vegetables in your stir-fry based on preference and availability. Your body's needs can fluctuate, so learn to tune in."
    }
  ],
  "motivation": "You've got this! Every meal, every rep, and every moment of rest brings you closer to a stronger, healthier, and more vibrant you. Embrace the journey, trust the process, and celebrate your progress along the way. Your dedication is your greatest asset \u2013 let's make this week a success!"
}
