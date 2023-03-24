import cProfile
import firstNonRepeatingCharacter

testString = 'asdgfdghsifuohsduifhsopfgesothpoiwq'

cProfile.run(f'firstNonRepeatingCharacter({testString})')
