from Functions.Problem831Code.blockspin_a import block_transform, magnetization, repeated_block_transformations, run_simulation

def main():

    size = 90

    # Temperatures to test
    temperatures = [
        1.0,
        2.269,   # Critical temperature
        5.0
    ]

    for T in temperatures:

        grid = run_simulation(size=size, T=T, post_sweeps = 100)

        print("\nShowing repeated RG transformations")
        repeated_block_transformations(grid, levels=4)

if __name__ == "__main__":
    main()