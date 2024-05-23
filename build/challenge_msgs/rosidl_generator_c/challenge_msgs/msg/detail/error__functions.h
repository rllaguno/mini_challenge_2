// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from challenge_msgs:msg/Error.idl
// generated code does not contain a copyright notice

#ifndef CHALLENGE_MSGS__MSG__DETAIL__ERROR__FUNCTIONS_H_
#define CHALLENGE_MSGS__MSG__DETAIL__ERROR__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "challenge_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "challenge_msgs/msg/detail/error__struct.h"

/// Initialize msg/Error message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * challenge_msgs__msg__Error
 * )) before or use
 * challenge_msgs__msg__Error__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
bool
challenge_msgs__msg__Error__init(challenge_msgs__msg__Error * msg);

/// Finalize msg/Error message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
void
challenge_msgs__msg__Error__fini(challenge_msgs__msg__Error * msg);

/// Create msg/Error message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * challenge_msgs__msg__Error__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
challenge_msgs__msg__Error *
challenge_msgs__msg__Error__create();

/// Destroy msg/Error message.
/**
 * It calls
 * challenge_msgs__msg__Error__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
void
challenge_msgs__msg__Error__destroy(challenge_msgs__msg__Error * msg);

/// Check for msg/Error message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
bool
challenge_msgs__msg__Error__are_equal(const challenge_msgs__msg__Error * lhs, const challenge_msgs__msg__Error * rhs);

/// Copy a msg/Error message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
bool
challenge_msgs__msg__Error__copy(
  const challenge_msgs__msg__Error * input,
  challenge_msgs__msg__Error * output);

/// Initialize array of msg/Error messages.
/**
 * It allocates the memory for the number of elements and calls
 * challenge_msgs__msg__Error__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
bool
challenge_msgs__msg__Error__Sequence__init(challenge_msgs__msg__Error__Sequence * array, size_t size);

/// Finalize array of msg/Error messages.
/**
 * It calls
 * challenge_msgs__msg__Error__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
void
challenge_msgs__msg__Error__Sequence__fini(challenge_msgs__msg__Error__Sequence * array);

/// Create array of msg/Error messages.
/**
 * It allocates the memory for the array and calls
 * challenge_msgs__msg__Error__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
challenge_msgs__msg__Error__Sequence *
challenge_msgs__msg__Error__Sequence__create(size_t size);

/// Destroy array of msg/Error messages.
/**
 * It calls
 * challenge_msgs__msg__Error__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
void
challenge_msgs__msg__Error__Sequence__destroy(challenge_msgs__msg__Error__Sequence * array);

/// Check for msg/Error message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
bool
challenge_msgs__msg__Error__Sequence__are_equal(const challenge_msgs__msg__Error__Sequence * lhs, const challenge_msgs__msg__Error__Sequence * rhs);

/// Copy an array of msg/Error messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_challenge_msgs
bool
challenge_msgs__msg__Error__Sequence__copy(
  const challenge_msgs__msg__Error__Sequence * input,
  challenge_msgs__msg__Error__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // CHALLENGE_MSGS__MSG__DETAIL__ERROR__FUNCTIONS_H_
