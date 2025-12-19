// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tf2_web_republisher_interfaces:srv/RepublishTFs.idl
// generated code does not contain a copyright notice

#ifndef TF2_WEB_REPUBLISHER_INTERFACES__SRV__DETAIL__REPUBLISH_T_FS__TRAITS_HPP_
#define TF2_WEB_REPUBLISHER_INTERFACES__SRV__DETAIL__REPUBLISH_T_FS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tf2_web_republisher_interfaces/srv/detail/republish_t_fs__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'timeout'
#include "builtin_interfaces/msg/detail/duration__traits.hpp"

namespace tf2_web_republisher_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const RepublishTFs_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: source_frames
  {
    if (msg.source_frames.size() == 0) {
      out << "source_frames: []";
    } else {
      out << "source_frames: [";
      size_t pending_items = msg.source_frames.size();
      for (auto item : msg.source_frames) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: target_frame
  {
    out << "target_frame: ";
    rosidl_generator_traits::value_to_yaml(msg.target_frame, out);
    out << ", ";
  }

  // member: angular_thres
  {
    out << "angular_thres: ";
    rosidl_generator_traits::value_to_yaml(msg.angular_thres, out);
    out << ", ";
  }

  // member: trans_thres
  {
    out << "trans_thres: ";
    rosidl_generator_traits::value_to_yaml(msg.trans_thres, out);
    out << ", ";
  }

  // member: rate
  {
    out << "rate: ";
    rosidl_generator_traits::value_to_yaml(msg.rate, out);
    out << ", ";
  }

  // member: timeout
  {
    out << "timeout: ";
    to_flow_style_yaml(msg.timeout, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RepublishTFs_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: source_frames
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.source_frames.size() == 0) {
      out << "source_frames: []\n";
    } else {
      out << "source_frames:\n";
      for (auto item : msg.source_frames) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: target_frame
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_frame: ";
    rosidl_generator_traits::value_to_yaml(msg.target_frame, out);
    out << "\n";
  }

  // member: angular_thres
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angular_thres: ";
    rosidl_generator_traits::value_to_yaml(msg.angular_thres, out);
    out << "\n";
  }

  // member: trans_thres
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "trans_thres: ";
    rosidl_generator_traits::value_to_yaml(msg.trans_thres, out);
    out << "\n";
  }

  // member: rate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rate: ";
    rosidl_generator_traits::value_to_yaml(msg.rate, out);
    out << "\n";
  }

  // member: timeout
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timeout:\n";
    to_block_style_yaml(msg.timeout, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RepublishTFs_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace tf2_web_republisher_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use tf2_web_republisher_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const tf2_web_republisher_interfaces::srv::RepublishTFs_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  tf2_web_republisher_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tf2_web_republisher_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const tf2_web_republisher_interfaces::srv::RepublishTFs_Request & msg)
{
  return tf2_web_republisher_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<tf2_web_republisher_interfaces::srv::RepublishTFs_Request>()
{
  return "tf2_web_republisher_interfaces::srv::RepublishTFs_Request";
}

template<>
inline const char * name<tf2_web_republisher_interfaces::srv::RepublishTFs_Request>()
{
  return "tf2_web_republisher_interfaces/srv/RepublishTFs_Request";
}

template<>
struct has_fixed_size<tf2_web_republisher_interfaces::srv::RepublishTFs_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<tf2_web_republisher_interfaces::srv::RepublishTFs_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<tf2_web_republisher_interfaces::srv::RepublishTFs_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace tf2_web_republisher_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const RepublishTFs_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: topic_name
  {
    out << "topic_name: ";
    rosidl_generator_traits::value_to_yaml(msg.topic_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RepublishTFs_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: topic_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "topic_name: ";
    rosidl_generator_traits::value_to_yaml(msg.topic_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RepublishTFs_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace tf2_web_republisher_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use tf2_web_republisher_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const tf2_web_republisher_interfaces::srv::RepublishTFs_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  tf2_web_republisher_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tf2_web_republisher_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const tf2_web_republisher_interfaces::srv::RepublishTFs_Response & msg)
{
  return tf2_web_republisher_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<tf2_web_republisher_interfaces::srv::RepublishTFs_Response>()
{
  return "tf2_web_republisher_interfaces::srv::RepublishTFs_Response";
}

template<>
inline const char * name<tf2_web_republisher_interfaces::srv::RepublishTFs_Response>()
{
  return "tf2_web_republisher_interfaces/srv/RepublishTFs_Response";
}

template<>
struct has_fixed_size<tf2_web_republisher_interfaces::srv::RepublishTFs_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<tf2_web_republisher_interfaces::srv::RepublishTFs_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<tf2_web_republisher_interfaces::srv::RepublishTFs_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<tf2_web_republisher_interfaces::srv::RepublishTFs>()
{
  return "tf2_web_republisher_interfaces::srv::RepublishTFs";
}

template<>
inline const char * name<tf2_web_republisher_interfaces::srv::RepublishTFs>()
{
  return "tf2_web_republisher_interfaces/srv/RepublishTFs";
}

template<>
struct has_fixed_size<tf2_web_republisher_interfaces::srv::RepublishTFs>
  : std::integral_constant<
    bool,
    has_fixed_size<tf2_web_republisher_interfaces::srv::RepublishTFs_Request>::value &&
    has_fixed_size<tf2_web_republisher_interfaces::srv::RepublishTFs_Response>::value
  >
{
};

template<>
struct has_bounded_size<tf2_web_republisher_interfaces::srv::RepublishTFs>
  : std::integral_constant<
    bool,
    has_bounded_size<tf2_web_republisher_interfaces::srv::RepublishTFs_Request>::value &&
    has_bounded_size<tf2_web_republisher_interfaces::srv::RepublishTFs_Response>::value
  >
{
};

template<>
struct is_service<tf2_web_republisher_interfaces::srv::RepublishTFs>
  : std::true_type
{
};

template<>
struct is_service_request<tf2_web_republisher_interfaces::srv::RepublishTFs_Request>
  : std::true_type
{
};

template<>
struct is_service_response<tf2_web_republisher_interfaces::srv::RepublishTFs_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TF2_WEB_REPUBLISHER_INTERFACES__SRV__DETAIL__REPUBLISH_T_FS__TRAITS_HPP_
