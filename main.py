import bufferless
import with_buffer

def main():

    # intensity (Probability) of updates generated by device
    lam = [0.3, 0.2, 0.1, 0.8]
    # Probability that transmission over link is successful for each device
    p = [0.5, 0.4, 0.6, 0.9]

    # Age-of-Information of three different scheduling
    # policies in system with no buffer.
    print("average AoI without buffer: ")
    
    rp_nb = bufferless.random_policy(lam, p)
    mp_nb = bufferless.max_age_policy(lam, p)
    wp_nb = bufferless.whittle_index_policy(lam, p)
    
    print("random policy: ", rp_nb)
    print("max age policy: ", mp_nb)
    print("Whittle Index: ", wp_nb)


    # Age-of-Information with buffer slot that stores last update.
    print("\naverage AoI with single buffer slot: ")
    
    rp_b = with_buffer.random_policy(lam, p)
    mp_b = with_buffer.max_age_policy(lam, p)
    wp_b = with_buffer.whittle_index_policy(lam, p)
    
    print("random policy: ", rp_b)
    print("max age policy: ", mp_b)
    print("Whittle Index: ", wp_b)


    return 0


main()
