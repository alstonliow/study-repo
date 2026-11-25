::: {.problem #prob-mit6006s20-5-q2 origin="external" source="mit6006s20-5-q2"}
**Power Plants**

The Boston electrical network contains $n$ power plants and $n^2$ buildings, pairs of which may be directly connected to each other via bidirectional wires. Every building is powered by either: having a wire directly to a power plant, or having a wire to another building that is recursively powered. Note that the network has the property that no building could be powered by more than one power plant (or else accounting would be ambiguous). Boston has secured funds to install an emergency generator in one of the power plants, which would provide backup power to all buildings powered by it, were the power plant to fail. Given a list $W$ of all the wires in the network, describe an $O(n^4)$-time algorithm to determine the power plant where Boston should install the generator that would provide backup power to the most buildings upon plant failure.
:::
