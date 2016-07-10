%: %.rs
	rustc $< -o $@_test --test
	./$@_test
	rustc $< -o $@
	./$@
