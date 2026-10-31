# Preserved infrastructure smoke test

Two real calls were made. Both exhausted the initial 180-token generation budget and produced incomplete JSON. They are retained, not silently dropped. No model-quality claim is drawn from this smoke test. The main exploratory run uses the same scenario selection and factorial conditions with a 512-token cap, frozen in a separate v2 directory before its inference begins. The budget change was chosen after observing these two truncations; neither run is preregistered.
