// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from signal_msg:msg/Signal.idl
// generated code does not contain a copyright notice

#ifndef SIGNAL_MSG__MSG__DETAIL__SIGNAL__STRUCT_HPP_
#define SIGNAL_MSG__MSG__DETAIL__SIGNAL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__signal_msg__msg__Signal __attribute__((deprecated))
#else
# define DEPRECATED__signal_msg__msg__Signal __declspec(deprecated)
#endif

namespace signal_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Signal_
{
  using Type = Signal_<ContainerAllocator>;

  explicit Signal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->name = "";
      this->num = 0l;
      this->reliability = 0.0f;
    }
  }

  explicit Signal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->name = "";
      this->num = 0l;
      this->reliability = 0.0f;
    }
  }

  // field types and members
  using _name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _name_type name;
  using _num_type =
    int32_t;
  _num_type num;
  using _reliability_type =
    float;
  _reliability_type reliability;

  // setters for named parameter idiom
  Type & set__name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->name = _arg;
    return *this;
  }
  Type & set__num(
    const int32_t & _arg)
  {
    this->num = _arg;
    return *this;
  }
  Type & set__reliability(
    const float & _arg)
  {
    this->reliability = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    signal_msg::msg::Signal_<ContainerAllocator> *;
  using ConstRawPtr =
    const signal_msg::msg::Signal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<signal_msg::msg::Signal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<signal_msg::msg::Signal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      signal_msg::msg::Signal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<signal_msg::msg::Signal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      signal_msg::msg::Signal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<signal_msg::msg::Signal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<signal_msg::msg::Signal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<signal_msg::msg::Signal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__signal_msg__msg__Signal
    std::shared_ptr<signal_msg::msg::Signal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__signal_msg__msg__Signal
    std::shared_ptr<signal_msg::msg::Signal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Signal_ & other) const
  {
    if (this->name != other.name) {
      return false;
    }
    if (this->num != other.num) {
      return false;
    }
    if (this->reliability != other.reliability) {
      return false;
    }
    return true;
  }
  bool operator!=(const Signal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Signal_

// alias to use template instance with default allocator
using Signal =
  signal_msg::msg::Signal_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace signal_msg

#endif  // SIGNAL_MSG__MSG__DETAIL__SIGNAL__STRUCT_HPP_
