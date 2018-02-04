on run argv
	tell application "Mail"
		set theMessages to messages of inbox whose message id = item 1 of argv
		set theMessage to item 1 of theMessages
		set theSender to sender of theMessage
		set senderAddress to extract address from theSender
		
		set allRules to the rules
		set friendlyAdsRule to rule "Freundliche Werbung"
		tell friendlyAdsRule
			set theConditions to rule conditions whose expression is senderAddress
			if theConditions is {} then
				-- no such rule condition exists yet, so let's add it!
				set newCondition to make new rule condition at end of rule conditions with properties {qualifier:equal to value, rule type:from header, expression:senderAddress}
				set qualifier of newCondition to equal to value -- for some reason the qualifier is ignored in the constructor (possible bug in the Mail Framework?), so we set it again here.
				return 1
			else
				-- oops, we have added this rule condition before, so no need to add it again.
				return 0
			end if
		end tell
	end tell
end run