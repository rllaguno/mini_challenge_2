// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from challenge_msgs:msg/Error.idl
// generated code does not contain a copyright notice

#ifndef CHALLENGE_MSGS__MSG__DETAIL__ERROR__STRUCT_HPP_
#define CHALLENGE_MSGS__MSG__DETAIL__ERROR__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__challenge_msgs__msg__Error __attribute__((deprecated))
#else
# define DEPRECATED__challenge_msgs__msg__Error __declspec(deprecated)
#endif

namespace challenge_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Error_
{
  using Type = Error_<ContainerAllocator>;

  explicit Error_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->center_error = 0.0f;
      this->points_error = 0.0f;
    }
  }

  explicit Error_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->center_error = 0.0f;
      this->points_error = 0.0f;
    }
  }

  // field types and members
  using _center_error_type =
    float;
  _center_error_type center_error;
  using _points_error_type =
    float;
  _points_error_type points_error;

  // setters for named parameter idiom
  Type & set__center_error(
    const float & _arg)
  {
    this->center_error = _arg;
    return *this;
  }
  Type & set__points_error(
    const float & _arg)
  {
    this->points_error = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    challenge_msgs::msg::Error_<ContainerAllocator> *;
  using ConstRawPtr =
    const challenge_msgs::msg::Error_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<challenge_msgs::msg::Error_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<challenge_msgs::msg::Error_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      challenge_msgs::msg::Error_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<challenge_msgs::msg::Error_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      challenge_msgs::msg::Error_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<challenge_msgs::msg::Error_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<challenge_msgs::msg::Error_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<challenge_msgs::msg::Error_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__challenge_msgs__msg__Error
    std::shared_ptr<challenge_msgs::msg::Error_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__challenge_msgs__msg__Error
    std::shared_ptr<challenge_msgs::msg::Error_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Error_ & other) const
  {
    if (this->center_error != other.center_error) {
      return false;
    }
    if (this->points_error != other.points_error) {
      return false;
    }
    return true;
  }
  bool operator!=(const Error_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Error_

// alias to use template instance with default allocator
using Error =
  challenge_msgs::msg::Error_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace challenge_msgs

#endif  // CHALLENGE_MSGS__MSG__DETAIL__ERROR__STRUCT_HPP_
