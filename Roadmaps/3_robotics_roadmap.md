# Robotics: Complete Roadmap, Resources & Career Guide

*Built for a BSCS student with a Computer Vision + ML background, full-stack dev experience, and a CLI/Linux-first workflow — moving into robotics/embodied systems.*

---

## What "Robotics" Actually Covers

Robotics is where software meets the physical world — it's the broadest and most hardware-adjacent of your four roadmaps (AV, multimodal AI, data science, and this one). It pulls together:

```
Perception (see/sense the environment)
    → Localization & Mapping (know where you are)
        → Planning (decide what to do)
            → Control (actuate motors/joints to do it)
                → (increasingly) Language/Reasoning (understand instructions — "embodied AI")
```

This overlaps heavily with your self-driving-cars roadmap — a self-driving car *is* a robot, just a constrained one (wheels, roads). This roadmap generalizes that to manipulators (arms), legged/mobile robots, drones, and the "given a robot, make it do something useful" problem broadly. If you've already worked through the AV roadmap, several phases here will feel familiar — I've noted the overlaps.

**Key difference from AV/pure software AI:** robotics is the one field on your list where you genuinely benefit from hands-on hardware, not just simulation. Budget for that below.

---

## PHASE 0 — Math & Physics Foundation (parallel, ongoing)

Overlaps almost entirely with your AV roadmap's Phase 0 — if you did that, you're most of the way here too.

| Topic | Why it matters | Resource |
|---|---|---|
| Linear Algebra | Coordinate transforms, rotations (quaternions, rotation matrices) | 3Blue1Brown *Essence of Linear Algebra*, MIT 18.06 OCW |
| Classical Mechanics | Forces, torques, kinematics — the physical basis of everything a robot does | Any intro physics mechanics course/textbook (e.g., OpenStax University Physics, free) |
| Linear Algebra for 3D rotations specifically | Robot arms/drones live and die by correct rotation math | *3D Rotations* chapter in any robotics textbook (see Phase 2) |
| Control Theory | PID, state-space, feedback control | Brian Douglas — *Control Systems Lectures* (YouTube, free) |
| Probability & Statistics | Sensor noise, Bayesian filtering | Khan Academy Probability, *Think Bayes* (free) |
| Differential Equations | Modeling dynamics of moving systems | MIT 18.03 OCW |

---

## PHASE 1 — Robot Kinematics & Dynamics (2 months)

This is the part that's genuinely new compared to your AV roadmap — self-driving cars are (mostly) simple rigid bodies on a plane; robot arms and legged robots have joints, which is a different math problem.

- **Course:** *Modern Robotics: Mechanics, Planning, and Control* (Northwestern, Coursera — free to audit) — this is **the** standout free course for robotics fundamentals, taught by Kevin Lynch, book is also free online
- **Book:** *Modern Robotics* (Lynch & Park) — free PDF, pairs directly with the course above
- **Topics:**
  - Forward kinematics (given joint angles, where's the end effector?)
  - Inverse kinematics (given a target position, what joint angles get you there?) — this is the harder, more important direction in practice
  - Jacobians — relating joint velocities to end-effector velocities (reused constantly)
  - Rigid body dynamics — how forces/torques translate to motion
  - Degrees of freedom, workspace analysis

**Milestone:** Implement forward and inverse kinematics for a simple simulated 2-link or 3-link robot arm in Python (no real hardware needed yet) and visualize it moving to target points.

---

## PHASE 2 — Perception for Robotics (1–2 months, you have a head start)

This is your CV641 background paying off directly.

- **Reuse most of Phase 2/3 from your AV roadmap** — object detection, segmentation, point cloud processing, camera calibration all apply directly here.
- **Additional robotics-specific topics:**
  - **Depth sensing:** structured light, stereo, time-of-flight (RGB-D cameras like RealSense/Kinect are the standard cheap sensor here)
  - **Tactile/force sensing** — a robotics-specific perception modality that doesn't come up in pure AV work; worth knowing conceptually even if you don't have hardware
  - **Object pose estimation** — not just "where is the object" but "what orientation is it in," critical for manipulation tasks (picking things up)

**Milestone:** If you get access to any RGB-D camera (even a phone with depth sensing, or simulated depth data), build a simple pipeline: detect an object → estimate its 3D pose.

---

## PHASE 3 — SLAM & Localization (1–2 months, direct overlap with AV roadmap)

If you did Phase 3 of your AV roadmap, this is largely the same material, generalized beyond wheeled vehicles.

- **Book:** *Probabilistic Robotics* (Thrun, Burgard, Fox) — same reference as AV roadmap, this is the canonical robotics text
- **Course:** *Robotics: Estimation and Learning* (Coursera, University of Pennsylvania — part of a broader Penn Robotics Specialization)
- **Topics:**
  - Extended/Unscented Kalman Filters, particle filters (same as AV roadmap)
  - SLAM: occupancy grid mapping, graph-based SLAM, visual SLAM (ORB-SLAM)
  - Sensor fusion (IMU + camera + LiDAR/depth)

**Milestone:** Run an existing open-source SLAM implementation (e.g., ORB-SLAM3) on a sample dataset or your own recorded video, and understand what's happening in the output map.

---

## PHASE 4 — Motion Planning & Control (2 months, direct overlap with AV roadmap)

- **Reuse Phase 4 from AV roadmap:** A*, RRT/RRT*, trajectory optimization, PID, MPC — all directly applicable.
- **Robotics-specific additions:**
  - **Configuration space planning** — for arms, "planning" happens in joint-angle space, not just physical (x,y) space; this is conceptually trickier than car path planning
  - **Motion planning libraries:** OMPL (Open Motion Planning Library) — the standard tool, used inside MoveIt (see Phase 5)
  - **Grasping/manipulation planning** — a robotics-specific planning problem (how do you approach and grip an object) that has no AV equivalent

**Milestone:** Use OMPL or MoveIt (see below) to plan a collision-free path for a simulated robot arm from one configuration to another around an obstacle.

---

## PHASE 5 — Middleware & Full-Stack Integration (ongoing — this is where robotics gets real)

- **ROS 2 (Robot Operating System)** — Learn this properly; it's even more central to robotics broadly than it was to your AV roadmap, since it's the standard across manipulation, mobile robots, and drones alike. Official ROS 2 tutorials (free) are the right starting point.
- **MoveIt** — the standard ROS-based motion planning framework for robot arms; sits on top of OMPL
- **Gazebo** (or newer **Gazebo Fortress/Ignition**) — the standard ROS-integrated physics simulator; this is your primary "robot" before you own hardware
- **URDF** — the standard format for describing a robot's physical structure (links, joints) to ROS/Gazebo — you'll need to read/write these

**Milestone:** Build a full simulated pipeline in Gazebo + ROS 2: a simulated mobile robot that perceives an obstacle (simulated camera/LiDAR), plans around it, and navigates to a goal using ROS 2's Navigation2 stack.

---

## PHASE 6 — Reinforcement Learning for Robotics (optional but increasingly important, 2 months)

This is more research-forward but is where a lot of current robotics excitement (and jobs) sit.

- **Course:** *Deep Reinforcement Learning* (Berkeley CS285) — free lectures online, the standard rigorous course
- **Book:** *Reinforcement Learning: An Introduction* (Sutton & Barto) — free PDF, the canonical RL textbook
- **Topics:**
  - Policy gradient methods, PPO (the most commonly used algorithm in practice)
  - Sim-to-real transfer — training in simulation, deploying on real hardware (a major open challenge)
  - Imitation learning (learning from demonstrations) — often more practical than pure RL for many tasks

**Milestone:** Train a simple RL policy in a simulated environment (OpenAI Gym / Gymnasium, or a robotics-specific sim like Isaac Gym / MuJoCo) to solve a basic control task (e.g., a robot arm reaching a target, or a simple legged locomotion task).

---

## PHASE 7 — Embodied AI: Where Robotics Meets Language/Multimodal AI (emerging, optional)

Given your multimodal AI roadmap, this is the natural convergence point of everything you're building across these tracks.

- **Paper/concept area:** "Embodied AI" — robots that take natural language instructions and act on them (e.g., Google's RT-2, SayCan)
- **Concept:** Vision-language-action (VLA) models — extending the VLM concepts from your multimodal roadmap with an "action" output
- This is genuinely cutting-edge and research-heavy; treat it as a "read papers and understand the direction" phase rather than something to master immediately, unless you go toward a research/grad-school path

---

## Hardware Reality Check

Robotics is the one field here where simulation-only can only take you so far. Options, roughly cheapest to most involved:

1. **Simulation only (free):** Gazebo + ROS 2, or PyBullet/MuJoCo for RL work. Do all of Phases 1–6 this way first — it's legitimate and how most people start.
2. **Small mobile robot kits:** TurtleBot (the standard ROS-compatible educational robot, but pricier and import/shipping into Pakistan may be a real obstacle) or a much cheaper DIY option — a Raspberry Pi + basic motor driver + ultrasonic/camera sensor build, which is very doable and commonly documented online.
3. **Robot arm kits:** Small, low-cost robot arm kits (servo-based, often under $100 equivalent) exist and are enough to practice inverse kinematics and basic manipulation concretely.
4. **Microcontroller basics (Arduino/ESP32):** Even without a full robot, learning to read sensors and drive motors from a microcontroller is valuable groundwork and very accessible/cheap.

**Practical suggestion given your context:** Start fully in simulation (free, no shipping/import issues), and if you want hardware, look at what's locally available in Pakistan (Arduino/Raspberry Pi ecosystem is generally accessible) before assuming you need imported robotics-specific kits.

---

## Capstone Options (pick one)

1. **Simulated autonomous mobile robot** — Gazebo + ROS 2 + Navigation2: a robot that maps an unknown environment (SLAM) and navigates to goals while avoiding obstacles. Most achievable solo, no hardware required.
2. **Robot arm pick-and-place pipeline** — simulated arm (MoveIt + Gazebo) that perceives an object (CV), estimates its pose, plans a grasp, and picks it up in simulation.
3. **Low-cost real hardware build** — Raspberry Pi/Arduino-based mobile robot with a camera, doing basic line-following or obstacle avoidance — most "real," most rewarding, most debugging pain (in a good way).
4. **RL-trained locomotion or manipulation task** — train a policy in MuJoCo/Isaac Gym for a specific task, document the sim-to-real gap conceptually even if you don't deploy to real hardware.

---

## Career Options

| Role | What it involves | Fits you if... |
|---|---|---|
| **Robotics Software Engineer** | ROS-based systems, integrating perception/planning/control | Broadest, most common robotics title — strong fit given your full-stack + CV background |
| **Perception Engineer (Robotics)** | Object detection, SLAM, sensor fusion for robots | Direct extension of your CV strength |
| **Motion Planning Engineer** | Path/motion planning, manipulation planning | If you enjoy the more math-heavy Phase 1/4 material |
| **Controls Engineer** | PID/MPC, often more EE-adjacent | Possible if you lean into the control theory side |
| **Robotics Research Engineer** | RL, embodied AI, novel algorithms — usually needs MS/PhD | Long-term path if research interests you |
| **Field Robotics Engineer** | Deploying/maintaining robots in real environments (agriculture, warehouses, inspection) | If you enjoy hands-on hardware work over pure software |

### Companies/ecosystem to know
- **Industrial/warehouse robotics:** Amazon Robotics, Locus Robotics, Fetch Robotics, Boston Dynamics (more legged/mobile robotics research-forward)
- **Manipulation/arms:** Universal Robots, Franka Robotics, ABB, KUKA (more traditional industrial, but growing software-defined side)
- **Agricultural/field robotics:** John Deere's autonomy division, various ag-tech startups — a genuinely underrated, growing niche
- **Drones:** DJI, Skydio, various defense/commercial drone companies
- **Research-heavy/embodied AI:** Google DeepMind's robotics team, Meta AI (robotics + embodied AI work), Physical Intelligence, various robotics-focused startups riding the current embodied-AI wave
- **Overlap reminder:** Everything in your **AV roadmap's company list** also counts here — AV is a subset of robotics from a hiring perspective, and skills transfer directly both ways.

### Realistic note on geography (same pattern as AV roadmap)
Robotics roles are similarly concentrated in the US, parts of Europe, Japan/South Korea (strong industrial robotics presence), and China. From Pakistan, the realistic near-term paths are largely the same as your AV roadmap: grad school abroad, remote-friendly software-focused robotics roles (ROS/perception/planning software doesn't require you to be physically near the hardware for a lot of the work), or building toward it via a strong open-source/simulation portfolio.

---

## Future Potential

- **Robotics is having a real inflection point right now**, driven by combining classical robotics (planning/control, decades of solid theory) with modern AI (foundation models, embodied AI, VLA models) — this is arguably the most exciting convergence in all of your four roadmaps.
- **Humanoid robotics** has seen a huge wave of investment recently (Tesla Optimus, Figure, Boston Dynamics' Atlas, various Chinese humanoid efforts) — much of this work sits exactly at the intersection of your CV, multimodal AI, and robotics roadmaps.
- **Field/agricultural robotics** and **warehouse/logistics robotics** are less flashy than humanoids but have clearer near-term commercial demand and are generally easier entry points than cutting-edge research robotics.
- **The software side of robotics (ROS, perception, planning) is increasingly remote-friendly** even when the hardware isn't — a growing number of robotics companies hire software-only remote roles for exactly this reason, which matters for your situation.
- Of your four roadmaps, robotics is the **most naturally unifying** — a lot of what you'd build here (SLAM, planning, control) is literally reusable in AV work, and the embodied-AI direction directly reuses your multimodal AI roadmap. If you're going to specialize deeply in one long-term direction, robotics is a reasonable "umbrella" that lets your AV and multimodal work both feed into it.

---

## Do's and Don'ts

### Do
- **Start in simulation, unapologetically.** Gazebo/ROS 2 is a completely legitimate way to build real robotics skill without hardware access/cost/import issues — don't let lack of hardware stop you from starting.
- **Learn ROS 2 deeply, not superficially.** It's the actual lingua franca of the field; a robotics engineer who doesn't know ROS well is a significant gap, the same way a web dev who doesn't know Git would be.
- **Lean into your CV strength immediately** — perception is directly transferable, and it's often the fastest way to make a robotics project feel "real" (a robot that can see and react is far more compelling than one that just executes a fixed script).
- **Get comfortable with C++ alongside Python** — ROS itself is mostly C++ under the hood (Python bindings exist and are fine for prototyping, but production robotics code leans C++ for real-time performance).
- **If you get any hardware at all** (even a $10 Arduino + ultrasonic sensor), do it — the debugging experience of real, noisy, physical sensors and actuators teaches things simulation alone doesn't (timing issues, sensor drift, mechanical slack).
- **Treat this as the natural "capstone" that ties your other roadmaps together** — a robot that sees (CV), understands instructions (NLP/multimodal), and acts (planning/control) is a genuinely impressive, differentiated portfolio piece if you get there.

### Don't
- **Don't assume "I know ML/CV so robotics will be easy."** The kinematics/dynamics/control math (Phase 1) is a genuinely different skill set from anything in your CV/ML background, and it's easy to underestimate how much rigor it needs.
- **Don't skip ROS thinking "I'll just write my own message-passing system."** This is a very common self-taught mistake — ROS solves a lot of hard, boring infrastructure problems (timing, message serialization, multi-process coordination) that aren't worth reinventing, and knowing ROS is itself a hireable skill.
- **Don't over-invest in expensive hardware early.** Simulation-first, then cheap microcontroller-based hardware, is the right order — don't feel pressure to buy a TurtleBot-equivalent before you've validated you enjoy the field.
- **Don't ignore the sim-to-real gap** — a policy or perception system that works perfectly in Gazebo/MuJoCo often fails on real hardware due to sensor noise, latency, and unmodeled dynamics; understand this is a real, unsolved-in-general problem, not a minor detail.
- **Don't treat RL as the default tool** — a lot of robotics tasks are still better solved with classical planning/control (Phase 1/4) than reinforcement learning; RL is powerful but often overused by people coming from an ML background who reach for it reflexively.
- **Don't neglect safety thinking, even in simulation** — real robots can hurt people or damage equipment; building the habit of thinking about failure modes and safe defaults early will matter a lot if you ever work with real hardware professionally.

---

## Suggested Order of Attack (given your current standing)

1. **Now–Month 2:** Kinematics/dynamics (Phase 1) — this is your genuinely new material, prioritize it since nothing in your background covers it yet.
2. **Month 1–3 (parallel):** ROS 2 basics (start of Phase 5) — get comfortable with the tooling early so later phases have somewhere to land.
3. **Month 2–3:** Perception (Phase 2) — fast for you, given your CV background; mostly about adapting existing skills to robotics-specific sensors/tasks.
4. **Month 3–4:** SLAM/localization (Phase 3) — significant overlap if you've done the AV roadmap's equivalent phase already.
5. **Month 4–5:** Motion planning/control (Phase 4) + full ROS/Gazebo integration (rest of Phase 5) — build your capstone here.
6. **Month 5–6+ (optional):** RL for robotics (Phase 6) if you want the research-forward angle, or go straight to a hardware build if you want the tangible/tactile angle instead.

---

*Robotics is unusual among your four roadmaps in that the core theory (kinematics, control, classical planning) is decades-old and very stable, while the AI-adjacent layer (embodied AI, VLA models, RL) is moving as fast as anything in multimodal AI. Revisit the classical phases rarely; revisit Phase 6/7 every few months, similar to your multimodal AI roadmap.*
