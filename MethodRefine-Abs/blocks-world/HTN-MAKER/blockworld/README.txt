The files in this directory consist of those that should be necessary to reproduce the Blocks World domain results published in "HTN-Maker: Learning HTNs with Minimal Additional Knowledge Engineering Required" by Chad Hogg, Hector Munoz-Avila, and Ugur Kuter published in Proceedings of the Twenty-Third AAAI Conference on Artificial Intelligence (AAAI-08).

The individual files are as follows:

`domain_strips.pddl` - A classical representation of the Blocks World domain, formatted for use by HTN-Maker and related programs.

`domain_ff.pddl` - A classical representation of the Blocks World domain, formatted for use with the FastForward planner.

`tasks.pddl` - A set of annotated tasks for the Blocks World domain, formatted for use by HTN-Maker and related programs.

`domain_empty.htn` - An HTN representation of the Blocks World domain but without any non-trivial methods, formatted for use by HTN-Maker and related programs.

`raw_probs/*.strips.prob.raw` - A set of all 561 unique classical planning problems in the Blocks World domain with 5 blocks that are in a single pile in the final state, formatted for use by the FastForward planner.

`htn_probs/*.htn.prob` - A set of 561 HTN planning problems, each of which is the equivalent of its corresponding file in `raw_probs/`.

`results/trial*/training_order.txt` - A list of 420 problem numbers.

`results/trial*/current_domain.htn` - An HTN representation of the Blocks World domain with methods learned from each of the problems listed in `results/trial*/training_order.txt` in order.

The intermediary results after processing each problem were not retained.
