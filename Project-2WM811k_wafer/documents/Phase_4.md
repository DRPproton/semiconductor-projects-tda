# Phase 4: Wafer Map Representation and Preprocessing

**Goal:** Represent maps consistently without destroying shape information.

**Tasks:**

- Confirm pixel/die values: background, good die, defective die.

- Convert each map into a binary failed-die mask and coordinate list.

- Preserve original aspect ratio when possible.

- Normalize coordinates to a common wafer coordinate system such as \[-1, 1\] x \[-1, 1\].

- Decide whether to resize images for CNN baselines separately from TDA features.

- Document every transformation.

**Expected output:** Preprocessing Strategy section.

**Key question:** Does preprocessing preserve the spatial signature?

**Stop condition:** Every map can be represented as failed-die coordinates plus metadata.