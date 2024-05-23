// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from challenge_msgs:msg/Error.idl
// generated code does not contain a copyright notice

#ifndef CHALLENGE_MSGS__MSG__DETAIL__ERROR__BUILDER_HPP_
#define CHALLENGE_MSGS__MSG__DETAIL__ERROR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "challenge_msgs/msg/detail/error__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace challenge_msgs
{

namespace msg
{

namespace builder
{

class Init_Error_points_error
{
public:
  explicit Init_Error_points_error(::challenge_msgs::msg::Error & msg)
  : msg_(msg)
  {}
  ::challenge_msgs::msg::Error points_error(::challenge_msgs::msg::Error::_points_error_type arg)
  {
    msg_.points_error = std::move(arg);
    return std::move(msg_);
  }

private:
  ::challenge_msgs::msg::Error msg_;
};

class Init_Error_center_error
{
public:
  Init_Error_center_error()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Error_points_error center_error(::challenge_msgs::msg::Error::_center_error_type arg)
  {
    msg_.center_error = std::move(arg);
    return Init_Error_points_error(msg_);
  }

private:
  ::challenge_msgs::msg::Error msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::challenge_msgs::msg::Error>()
{
  return challenge_msgs::msg::builder::Init_Error_center_error();
}

}  // namespace challenge_msgs

#endif  // CHALLENGE_MSGS__MSG__DETAIL__ERROR__BUILDER_HPP_
