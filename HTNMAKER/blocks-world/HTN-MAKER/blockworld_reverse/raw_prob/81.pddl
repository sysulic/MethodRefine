( define ( problem probname )
	( :domain blocks4 )
	( :requirements :strips :typing :equality )
	( :objects
		block1 - block
		block2 - block
		block3 - block
		block4 - block
		block5 - block
	)
	( :init
		( on block5 block1 )
		( on block3 block5 )
		( on block1 block4 )
		( on-table block2 )
		( on-table block4 )
		( clear block3 )
		( clear block2 )
		( hand-empty )
	)
	( :goal
		( and
			( on-table block1 )
			( on block2 block1 )
			( on block3 block2 )
			( on block4 block3 )
			( on block5 block4 )
			( clear block5 )
		)
	)
)