::: {.problem #prob-mit1803ps-19-q1 origin="external" source="mit1803ps-19-q1"}
[Models and complex gain] This problem employs the Mathlet Amplitude and Phase: Second Order I, which illustrates the steady state sinusoidal system response of a spring/mass/dashpot system driven through the spring, as discussed in the session on Gain and Phase Lag. The amplitude of the input signal is 1, so the amplitude of the system response is the gain. Select $b = 0.5$, $k = 4.00$, and $\omega = 2.00$. Animate the system.

(a) Verify the displayed values of time lag and gain.

(b) The input signal in this system is the position $y(t) = \cos(\omega t)$ of the top of the spring (the cyan box). The system response is the position of the mass (the yellow box), and we are looking just at the steady state solution $x(t)$. Determine the complex gain for this system. From it determine the gain of the system, as a function of $\omega$. Finally determine $\tan\phi$ where $\phi$ is the phase lag.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::

::: {.problem #prob-mit1803ps-19-q2 origin="external" source="mit1803ps-19-q2"}
[Frequency response] This problem will use the applet Amplitude and Phase: Second Order I again (as in a previous problem). Set $k = 4.00$, $b = 0.50$. These settings will be in force for parts (a) through (c).

(a) In a previous problem you studied the response of this system when $\omega = 2.00$. The gain is pretty large with that setting. Let's investigate the gain for other values of $\omega$. You can see a graph of the gain as a function of the input circular frequency $\omega$ by invoking [Bode Plots]. The top window shows the gain as a function of $\omega$, and the bottom window graphs $-\phi$ as a function of $\omega$. Move the $\omega$ slider and verify that these readings correspond to the graph of the system response at left. You can see a readout of the value of the gain and the phase lag for the selected value of $\omega$ by rolling the cursor over the relevant window.

From your experimentation with the applet, do you believe that the gain maximal for $\omega = 2.00$, or is the "practical resonance" peak at a different value of $\omega$?

In the previous problem mentioned you wrote down a formula for the gain as a function of $\omega$ (for these values of $k$ and $b$), $g(\omega)$. Now find the value $\omega = \omega_r$ which maximizes $g(\omega)$. (Hint: it'll be easier to minimize the square of the denominator.) Is it at $\omega = 2$? Finally, what is the maximal gain?

(b) Experiment to find the value of $\omega$ giving phase lag as close to $45^\circ$ as you can. In previous problem mentioned you also gave a formula for $\tan\phi$. Determine the positive value of $\omega$ for which the phase lag equals $45^\circ$. Compare.

(c) Now invoke the [Nyquist Plot]. This shows the trajectory of the complex gain $H(\omega)$ as $\omega$ runs from $0$ to $\infty$. The value of $H(\omega)$ corresponding to the selected value of $\omega$ is shown as a yellow diamond. This means that the length of the yellow strut equals the gain, and the size of the green arc equals the phase lag. Again grab the $\omega$ slider and move it slowly from $0$ to $4$. Please submit a sketch of the Nyquist plot with $\omega$ such that $\phi(\omega)$ is as close to $\frac\pi4$ as you can get it.

(d) Finally, set $\omega = 2$ and leave $k = 4.00$, but adjust the value of $b$ by grabbing the $b$ slider. What do you observe about the position of the yellow strut in the Nyquist plot? Try setting $k$ to a different value, and adjust $\omega$ so that the phase lag is close to $\frac\pi2$. Now vary $b$ and comment on what happens to the phase lag. Please explain this observation as follows. Write down a formula for the complex gain $H(\omega)$ for general values of $b$, $k$, and $\omega$. What does $\phi = \frac\pi2$ say about the complex gain? Finally, what relationship does this imply about $b$, $k$, and $\omega$? Does this relationship explain your observation?

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::

::: {.problem #prob-mit1803ps-20-q1 origin="external" source="mit1803ps-20-q1"}
[Series RLC circuits; amplitude and phase] Open the Mathlet Series RLC Circuit. Here we will focus entirely on the current response, so it will be clearer if the check boxes labelled $V_R$, $V_L$, $V_C$, are left unchecked. But click twice on the $I$ box, to make a green curve appear in the graphing window, representing the current through any point in the circuit as a function of time.

The Mathlet uses the International System of Units, SI, formerly known as the mks (meter-kilogram-second) system. The equation
$$L\ddot I + R\dot I + (1/C)I = \dot V$$
is correct when:

the resistance $R$ is measured in ohms, $\Omega$,

the inductance $L$ is measured in H, henries,

the capacitance $C$ is measured in farads, F,

the voltage $V$ is measured in volts, also denoted V,

the current $I$ is measured in amperes, A.

The slider displays millihenries, mH (1 mH $= 10^{-3}$ H) and microfarads, $\mu$F (1 $\mu$F $= 10^{-6}$ F), and milliseconds, ms (1 ms $= 10^{-3}$ sec).

The Mathlet studies a sinusoidal input signal $V(t) = V_0\sin(\omega t)$. Play around with the various sliders and watch the effect on the (blue) voltage curve and the (green) current curve.

(a) By experimenting, identify a few values of the system parameters $R$, $L$, $C$, $V_0$, $\omega$, for which the current and the voltage are perfectly in phase. For example, if $L = 500$ mH and $\omega = 200$ radians/second, what values of $R$, $C$, and $V_0$ put $I$ in phase with $V$?

(b) Now calculate the relationship between the system parameters which leads to $I$ and $V$ being in phase. Do your experiments align with your calculations?

(c) Set $R = 100\ \Omega$, $L = 1000$ mH, $C = 100\ \mu$F, $V_0 = 500$ V. Vary $\omega$ and watch the action. For what value of $\omega$ is the amplitude of $I(t)$ maximal? What is that amplitude (in amps)? What is the phase lag between the input signal, $V_0\sin(\omega t)$, and the system response, $I(t)$, for that value of $\omega$?

(d) Verify the three observations made in (c) computationally. You should be able to do this for general values of $R$, $L$, $C$, $V_0$.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::

::: {.problem #prob-mit1803ps-20-q2 origin="external" source="mit1803ps-20-q2"}
AM Radio Tuning and LRC Circuits

An LRC circuit can be modeled using the same DE as in the previous problem. Specifically,
$$LI'' + RI' + \frac1C I = E' .$$
Where $I$ = current in amps, $L$ = inductance in henries, $R$ = resistance in ohms, $C$ = capacitance in farads and $E$ = input EMF in volts. Often the important output is the voltage drop $V_R$ across the resistor. Ohm's law tells us $V_R = RI$. This gives us the DE
$$LV_R'' + RV_R' + \frac1C V_R = RE' .$$

(a) Assume $E = E_0\cos(\omega t)$ and solve the DE for $V_R$ in phase-amplitude form.

(b) Open the 'LRC Filter Applet'. This applet models an LRC circuit with input voltage a superposition of sine waves. Play with the applet –be sure to learn how to vary $\omega_1$ and $\omega_2$ by dragging the dots on the amplitude plot.

Describe what happens to the amplitude response plot as $L$, $R$ and $C$ are varied.

(c) An LRC circuit can be used as part of a simple AM radio tuner. In an AM radio broadcast the signal is given by $a\cos(\omega t)$ where $\omega$ is the 'carrier' frequency (between 530 and 1600 khz). To really carry information the amplitude $a$ must vary –this is the amplitude modulation– but, we will ignore this right here.

The range of values for this simple variable capacitor AM radio tuner is $L \approx .5$ microhenries, $R$ is the resistance in the wire (very small) and $C$ is between .02 and .2 microfarads. To keep things simple we will use different ranges however the idea is the same.

In the LRC Filter applet set $\omega_1 = 1$ and $\omega_2 = 4$ (set them as close as you can on your system). Set the input amplitudes $a$ and $b$ to 1. Find settings for $L$, $R$ and $C$ so that the output filters out the $\omega_2$ part of the signal i.e. the output looks (a lot) like a sine wave of frequency $\omega_1$. Give your values for $L$, $R$ and $C$.

How does the quality of the filter change as you vary $R$?

(d) An antenna on a radio picks up electomagnetic signals from all frequencies. It responds by outputing a signal consisting of voltages at each of these frequencies. This signal is used as input to a tuner circuit.

Using the applet, set $L = 1$, $R = .5$. Now, vary $C$ and then explain why a variable capacitor circuit could be used as an AM radio tuner.

(e) Show that the natural frequency (undamped, unforced resonant frequency) of the system is $\omega_0 = 1/\sqrt{LC}$. Show that even with damping, i.e., $R > 0$, $\omega_0$ is always the practical resonant frequency. (Hint: this can be done without calculus by writing $A(\omega)$ in the proper way.)

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::
