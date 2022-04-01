/*------------------------------------------------------------------------*
 Project: Support Recruitment Test

 Copyright (C) 2022 Nintendo, All rights reserved.

 These coded instructions, statements, and computer programs contain proprietary
 information of Nintendo and/or its licensed developers and are protected by
 national and international copyright laws. They may not be disclosed to third
 parties or copied or duplicated in any form, in whole or in part, without the
 prior written consent of Nintendo.

 The content herein is highly confidential and should be handled accordingly.
*------------------------------------------------------------------------*/
#include "nerd/features.h"

#include <cstddef>

#if __cplusplus < 201703L
#error The source is not compiled in c++17 mode
#endif

#include <iostream>

#define ASSERT_EQUAL(a, b)                                                                    \
    do                                                                                        \
    {                                                                                         \
        if ((a) != (b))                                                                       \
        {                                                                                     \
            std::cerr << "FAILURE: expected " #a "=" << (a) << " got " #b "=" << (b) << "\n"; \
            return false;                                                                     \
        }                                                                                     \
    } while (0)

namespace
{
    bool test_add()
    {
        for (int i = 0; i < 512; ++i)
        {
            for (int j = 0; j < 512; ++j)
            {
                int expected = i + j;
                int result = nerd_add(i, j);
                ASSERT_EQUAL(expected, result);
            }
        }

        return true;
    }

    bool test_mul()
    {
        for (int i = 0; i < 512; ++i)
        {
            for (int j = 0; j < 512; ++j)
            {
                int expected = i * j;
                int result = nerd_mul(i, j);
                ASSERT_EQUAL(expected, result);
            }
        }

        return true;
    }

    bool test_fail()
    {
        return false;
    }
} // namespace anonymous

extern "C" int main(int argc, char **argv)
{
    std::cout << "Test program\n";

    struct
    {
        const char *name;
        bool (*func)();
    } test_list[] = {
        {"Addition", test_add},
        {"Multiplication", test_mul},
        {"WontWork", test_fail}};
    static constexpr auto test_list_len = sizeof(test_list) / sizeof(test_list[0]);

    bool success = true;
    size_t failures = 0;
    size_t successes = 0;

    size_t i;
    for (i = 0; i < test_list_len; ++i)
    {
        bool result = test_list[i].func();
        if (result)
        {
            std::cout << "[ SUCCESS ] TestSuite." << test_list[i].name << "\n";
            successes++;
        }
        else
        {
            std::cout << "[ FAILURE ] TestSuite." << test_list[i].name << "\n";
            failures++;
        }
        success = success && result;
    }

    std::cout << "[ RESULTS ] " << successes << "/" << i << "\n";

    return success ? EXIT_SUCCESS : EXIT_FAILURE;
}