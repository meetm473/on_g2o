#include "graph_types.h"

#include <g2o/core/factory.h>
#include <g2o/stuff/macros.h>

namespace g2o {
  namespace viman {

  G2O_REGISTER_TYPE_GROUP(viman);

  G2O_REGISTER_TYPE(VM_VERTEX_SE3, VertexSE3);
  G2O_REGISTER_TYPE(VM_VERTEX_POINT_XY, VertexPointXYZ);

  G2O_REGISTER_TYPE(VM_PARAMS_SE3_OFFSET, ParameterSE3Offset);

  G2O_REGISTER_TYPE(VM_CACHE_SE3_OFFSET, CacheSE3Offset);

  G2O_REGISTER_TYPE(VM_EDGE_SE3, EdgeSE3);
  G2O_REGISTER_TYPE(VM_EDGE_SE3_POINT_XYZ, EdgeSE3PointXYZ);

  }
} // end namespace
