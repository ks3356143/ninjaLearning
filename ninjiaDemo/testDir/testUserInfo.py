result_info = {
    "success": True,
    "message": "请求成功",
    "code": 200,
    "data": {
        "user": {
            "id": 1,
            "username": "superAdmin",
            "user_type": "100",
            "nickname": "超级管理员",
            "phone": "13888888888",
            "email": "admin123@adminmine.com",
            "avatar": "https://img.mineadmin.com/uploadfile/20230330/499990370432749568.jpg",
            "signed": "Today is very good！",
            "dashboard": "statistics",
            "status": 2,
            "login_ip": "110.191.213.187",
            "login_time": "2023-06-01 16:44:02",
            "backend_setting": {
                "mode": "light",
                "tag": True,
                "menuCollapse": False,
                "menuWidth": 220,
                "layout": "classic",
                "skin": "mine",
                "i18n": False,
                "language": "zh_CN",
                "animation": "ma-slide-down",
                "color": "#165DFF"
            },
            "created_by": 0,
            "updated_by": 1,
            "created_at": "2022-08-01 02:35:14",
            "updated_at": "2023-06-01 16:44:02",
            "remark": None
        },
        "roles": [
            "superAdmin"
        ],
        "routers": [
            {
                "id": 1000,
                "parent_id": 0,
                "name": "permission",
                "component": "",
                "path": "/permission",
                "redirect": None,
                "meta": {
                    "type": "M",
                    "icon": "ma-icon-permission",
                    "title": "权限",
                    "hidden": False,
                    "hiddenBreadcrumb": False
                },
                "children": [
                    {
                        "id": 1100,
                        "parent_id": 1000,
                        "name": "system:user",
                        "component": "system/user/index",
                        "path": "/user",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-user",
                            "title": "用户管理",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        # "children": [
                        #     {
                        #         "id": 1101,
                        #         "parent_id": 1100,
                        #         "name": "system:user:index",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户列表",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1102,
                        #         "parent_id": 1100,
                        #         "name": "system:user:recycle",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户回收站列表",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1103,
                        #         "parent_id": 1100,
                        #         "name": "system:user:save",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户保存",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1104,
                        #         "parent_id": 1100,
                        #         "name": "system:user:update",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户更新",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1105,
                        #         "parent_id": 1100,
                        #         "name": "system:user:delete",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户删除",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1106,
                        #         "parent_id": 1100,
                        #         "name": "system:user:read",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户读取",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1107,
                        #         "parent_id": 1100,
                        #         "name": "system:user:recovery",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户恢复",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1108,
                        #         "parent_id": 1100,
                        #         "name": "system:user:realDelete",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户真实删除",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1109,
                        #         "parent_id": 1100,
                        #         "name": "system:user:import",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户导入",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1110,
                        #         "parent_id": 1100,
                        #         "name": "system:user:export",
                        #         "component": None,
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": None,
                        #             "title": "用户导出",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1111,
                        #         "parent_id": 1100,
                        #         "name": "system:user:changeStatus",
                        #         "component": "",
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": "",
                        #             "title": "用户状态改变",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1112,
                        #         "parent_id": 1100,
                        #         "name": "system:user:initUserPassword",
                        #         "component": "",
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": "",
                        #             "title": "用户初始化密码",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1113,
                        #         "parent_id": 1100,
                        #         "name": "system:user:cache",
                        #         "component": "",
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": "",
                        #             "title": "更新用户缓存",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     },
                        #     {
                        #         "id": 1114,
                        #         "parent_id": 1100,
                        #         "name": "system:user:homePage",
                        #         "component": "",
                        #         "path": "/",
                        #         "redirect": None,
                        #         "meta": {
                        #             "type": "B",
                        #             "icon": "",
                        #             "title": "设置用户首页",
                        #             "hidden": True,
                        #             "hiddenBreadcrumb": False
                        #         }
                        #     }
                        # ]
                    },
                    {
                        "id": 1400,
                        "parent_id": 1000,
                        "name": "system:role",
                        "component": "system/role/index",
                        "path": "/role",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-role",
                            "title": "角色管理",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 1401,
                                "parent_id": 1400,
                                "name": "system:role:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1402,
                                "parent_id": 1400,
                                "name": "system:role:recycle",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色回收站",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1403,
                                "parent_id": 1400,
                                "name": "system:role:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色保存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1404,
                                "parent_id": 1400,
                                "name": "system:role:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色更新",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1405,
                                "parent_id": 1400,
                                "name": "system:role:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1406,
                                "parent_id": 1400,
                                "name": "system:role:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色读取",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1407,
                                "parent_id": 1400,
                                "name": "system:role:recovery",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色恢复",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1408,
                                "parent_id": 1400,
                                "name": "system:role:realDelete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色真实删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1409,
                                "parent_id": 1400,
                                "name": "system:role:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色导入",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1410,
                                "parent_id": 1400,
                                "name": "system:role:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "角色导出",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1411,
                                "parent_id": 1400,
                                "name": "system:role:changeStatus",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "角色状态改变",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1412,
                                "parent_id": 1400,
                                "name": "system:role:menuPermission",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "更新菜单权限",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1413,
                                "parent_id": 1400,
                                "name": "system:role:dataPermission",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "更新数据权限",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 1300,
                        "parent_id": 1000,
                        "name": "system:dept",
                        "component": "system/dept/index",
                        "path": "/dept",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-dept",
                            "title": "部门管理",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 1301,
                                "parent_id": 1300,
                                "name": "system:dept:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1302,
                                "parent_id": 1300,
                                "name": "system:dept:recycle",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门回收站",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1303,
                                "parent_id": 1300,
                                "name": "system:dept:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门保存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1304,
                                "parent_id": 1300,
                                "name": "system:dept:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门更新",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1305,
                                "parent_id": 1300,
                                "name": "system:dept:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1306,
                                "parent_id": 1300,
                                "name": "system:dept:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门读取",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1307,
                                "parent_id": 1300,
                                "name": "system:dept:recovery",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门恢复",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1308,
                                "parent_id": 1300,
                                "name": "system:dept:realDelete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门真实删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1309,
                                "parent_id": 1300,
                                "name": "system:dept:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门导入",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1310,
                                "parent_id": 1300,
                                "name": "system:dept:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "部门导出",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1311,
                                "parent_id": 1300,
                                "name": "system:dept:changeStatus",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "部门状态改变",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 1200,
                        "parent_id": 1000,
                        "name": "system:menu",
                        "component": "system/menu/index",
                        "path": "/menu",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-menu",
                            "title": "菜单管理",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 1201,
                                "parent_id": 1200,
                                "name": "system:menu:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1202,
                                "parent_id": 1200,
                                "name": "system:menu:recycle",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单回收站",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1203,
                                "parent_id": 1200,
                                "name": "system:menu:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单保存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1204,
                                "parent_id": 1200,
                                "name": "system:menu:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单更新",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1205,
                                "parent_id": 1200,
                                "name": "system:menu:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1206,
                                "parent_id": 1200,
                                "name": "system:menu:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单读取",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1207,
                                "parent_id": 1200,
                                "name": "system:menu:recovery",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单恢复",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1208,
                                "parent_id": 1200,
                                "name": "system:menu:realDelete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单真实删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1209,
                                "parent_id": 1200,
                                "name": "system:menu:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单导入",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1210,
                                "parent_id": 1200,
                                "name": "system:menu:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "菜单导出",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 1500,
                        "parent_id": 1000,
                        "name": "system:post",
                        "component": "system/post/index",
                        "path": "/post",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-post",
                            "title": "岗位管理",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 1501,
                                "parent_id": 1500,
                                "name": "system:post:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1502,
                                "parent_id": 1500,
                                "name": "system:post:recycle",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位回收站",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1503,
                                "parent_id": 1500,
                                "name": "system:post:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位保存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1504,
                                "parent_id": 1500,
                                "name": "system:post:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位更新",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1505,
                                "parent_id": 1500,
                                "name": "system:post:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1506,
                                "parent_id": 1500,
                                "name": "system:post:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位读取",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1507,
                                "parent_id": 1500,
                                "name": "system:post:recovery",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位恢复",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1508,
                                "parent_id": 1500,
                                "name": "system:post:realDelete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位真实删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1509,
                                "parent_id": 1500,
                                "name": "system:post:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位导入",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1510,
                                "parent_id": 1500,
                                "name": "system:post:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "岗位导出",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 1511,
                                "parent_id": 1500,
                                "name": "system:post:changeStatus",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "岗位状态改变",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "id": 2000,
                "parent_id": 0,
                "name": "dataCenter",
                "component": "",
                "path": "/dataCenter",
                "redirect": None,
                "meta": {
                    "type": "M",
                    "icon": "icon-storage",
                    "title": "数据",
                    "hidden": False,
                    "hiddenBreadcrumb": False
                },
                "children": [
                    {
                        "id": 2100,
                        "parent_id": 2000,
                        "name": "system:dict",
                        "component": "system/dict/index",
                        "path": "/dict",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-dict",
                            "title": "数据字典",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 2101,
                                "parent_id": 2100,
                                "name": "system:dict:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2102,
                                "parent_id": 2100,
                                "name": "system:dict:recycle",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典回收站",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2103,
                                "parent_id": 2100,
                                "name": "system:dict:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典保存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2104,
                                "parent_id": 2100,
                                "name": "system:dict:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典更新",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2105,
                                "parent_id": 2100,
                                "name": "system:dict:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2106,
                                "parent_id": 2100,
                                "name": "system:dict:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典读取",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2107,
                                "parent_id": 2100,
                                "name": "system:dict:recovery",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典恢复",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2108,
                                "parent_id": 2100,
                                "name": "system:dict:realDelete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典真实删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2109,
                                "parent_id": 2100,
                                "name": "system:dict:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典导入",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2110,
                                "parent_id": 2100,
                                "name": "system:dict:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据字典导出",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2112,
                                "parent_id": 2100,
                                "name": "system:dataDict:changeStatus",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "字典状态改变",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 2200,
                        "parent_id": 2000,
                        "name": "system:attachment",
                        "component": "system/attachment/index",
                        "path": "/attachment",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-attach",
                            "title": "附件管理",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 2202,
                                "parent_id": 2200,
                                "name": "system:attachment:index",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "附件列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2203,
                                "parent_id": 2200,
                                "name": "system:attachment:recycle",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "附件回收站",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2204,
                                "parent_id": 2200,
                                "name": "system:attachment:realDelete",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "附件真实删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 2300,
                        "parent_id": 2000,
                        "name": "system:dataMaintain",
                        "component": "system/dataMaintain/index",
                        "path": "/dataMaintain",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-db",
                            "title": "数据表维护",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 2304,
                                "parent_id": 2300,
                                "name": "system:dataMaintain:optimize",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "数据表优化",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2201,
                                "parent_id": 2300,
                                "name": "system:attachment:delete",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "附件删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2301,
                                "parent_id": 2300,
                                "name": "system:dataMaintain:index",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "数据表列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2302,
                                "parent_id": 2300,
                                "name": "system:dataMaintain:detailed",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "数据表详细",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2303,
                                "parent_id": 2300,
                                "name": "system:dataMaintain:fragment",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "数据表清理碎片",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 2700,
                        "parent_id": 2000,
                        "name": "system:notice",
                        "component": "system/notice/index",
                        "path": "/notice",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-bulb",
                            "title": "系统公告",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 2701,
                                "parent_id": 2700,
                                "name": "system:notice:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2702,
                                "parent_id": 2700,
                                "name": "system:notice:recycle",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告回收站",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2703,
                                "parent_id": 2700,
                                "name": "system:notice:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告保存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2704,
                                "parent_id": 2700,
                                "name": "system:notice:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告更新",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2705,
                                "parent_id": 2700,
                                "name": "system:notice:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2706,
                                "parent_id": 2700,
                                "name": "system:notice:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告读取",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2707,
                                "parent_id": 2700,
                                "name": "system:notice:recovery",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告恢复",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2708,
                                "parent_id": 2700,
                                "name": "system:notice:realDelete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告真实删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2709,
                                "parent_id": 2700,
                                "name": "system:notice:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告导入",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 2710,
                                "parent_id": 2700,
                                "name": "system:notice:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "系统公告导出",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 2500,
                        "parent_id": 2000,
                        "name": "apps",
                        "component": "",
                        "path": "/apps",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-apps",
                            "title": "应用中心",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 2510,
                                "parent_id": 2500,
                                "name": "system:appGroup",
                                "component": "system/appGroup/index",
                                "path": "/appGroup",
                                "redirect": None,
                                "meta": {
                                    "type": "M",
                                    "icon": "ma-icon-group",
                                    "title": "应用分组",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                },
                                "children": [
                                    {
                                        "id": 2511,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:index",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组列表",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2512,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:recycle",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组回收站",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2513,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:save",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组保存",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2514,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:update",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组更新",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2515,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:delete",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2516,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:read",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组读取",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2517,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:recovery",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组恢复",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2518,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:realDelete",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组真实删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2519,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:import",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组导入",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2520,
                                        "parent_id": 2510,
                                        "name": "system:appGroup:export",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用分组导出",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    }
                                ]
                            },
                            {
                                "id": 2530,
                                "parent_id": 2500,
                                "name": "system:app",
                                "component": "system/app/index",
                                "path": "/app",
                                "redirect": None,
                                "meta": {
                                    "type": "M",
                                    "icon": "icon-archive",
                                    "title": "应用管理",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                },
                                "children": [
                                    {
                                        "id": 2531,
                                        "parent_id": 2530,
                                        "name": "system:app:index",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用列表",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2532,
                                        "parent_id": 2530,
                                        "name": "system:app:recycle",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用回收站",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2533,
                                        "parent_id": 2530,
                                        "name": "system:app:save",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用保存",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2534,
                                        "parent_id": 2530,
                                        "name": "system:app:update",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用更新",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2535,
                                        "parent_id": 2530,
                                        "name": "system:app:delete",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2536,
                                        "parent_id": 2530,
                                        "name": "system:app:read",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用读取",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2537,
                                        "parent_id": 2530,
                                        "name": "system:app:recovery",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用恢复",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2538,
                                        "parent_id": 2530,
                                        "name": "system:app:realDelete",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用真实删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2539,
                                        "parent_id": 2530,
                                        "name": "system:app:import",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用导入",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2540,
                                        "parent_id": 2530,
                                        "name": "system:app:export",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "应用导出",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2541,
                                        "parent_id": 2530,
                                        "name": "system:app:bind",
                                        "component": "",
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": "",
                                            "title": "应用绑定接口",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": 2600,
                        "parent_id": 2000,
                        "name": "apis",
                        "component": "",
                        "path": "/apis",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-common",
                            "title": "应用接口",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 2610,
                                "parent_id": 2600,
                                "name": "system:apiGroup",
                                "component": "system/apiGroup/index",
                                "path": "/apiGroup",
                                "redirect": None,
                                "meta": {
                                    "type": "M",
                                    "icon": "ma-icon-group",
                                    "title": "接口分组",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                },
                                "children": [
                                    {
                                        "id": 2611,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:index",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组列表",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2612,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:recycle",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组回收站",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2613,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:save",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组保存",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2614,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:update",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组更新",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2615,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:delete",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2616,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:read",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组读取",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2617,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:recovery",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组恢复",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2618,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:realDelete",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组真实删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2619,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:import",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组导入",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2620,
                                        "parent_id": 2610,
                                        "name": "system:apiGroup:export",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口分组导出",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    }
                                ]
                            },
                            {
                                "id": 2630,
                                "parent_id": 2600,
                                "name": "system:api",
                                "component": "system/api/index",
                                "path": "/api",
                                "redirect": None,
                                "meta": {
                                    "type": "M",
                                    "icon": "icon-mind-mapping",
                                    "title": "接口管理",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                },
                                "children": [
                                    {
                                        "id": 2631,
                                        "parent_id": 2630,
                                        "name": "system:api:index",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口列表",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2632,
                                        "parent_id": 2630,
                                        "name": "system:api:recycle",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口回收站",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2633,
                                        "parent_id": 2630,
                                        "name": "system:api:save",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口保存",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2634,
                                        "parent_id": 2630,
                                        "name": "system:api:update",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口更新",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2635,
                                        "parent_id": 2630,
                                        "name": "system:api:delete",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2636,
                                        "parent_id": 2630,
                                        "name": "system:api:read",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口读取",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2637,
                                        "parent_id": 2630,
                                        "name": "system:api:recovery",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口恢复",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2638,
                                        "parent_id": 2630,
                                        "name": "system:api:realDelete",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口真实删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2639,
                                        "parent_id": 2630,
                                        "name": "system:api:import",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口导入",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 2640,
                                        "parent_id": 2630,
                                        "name": "system:api:export",
                                        "component": None,
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": None,
                                            "title": "接口导出",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "id": 3000,
                "parent_id": 0,
                "name": "monitor",
                "component": "",
                "path": "/monitor",
                "redirect": None,
                "meta": {
                    "type": "M",
                    "icon": "icon-desktop",
                    "title": "监控",
                    "hidden": False,
                    "hiddenBreadcrumb": False
                },
                "children": [
                    {
                        "id": 3200,
                        "parent_id": 3000,
                        "name": "system:monitor:server",
                        "component": "system/monitor/server/index",
                        "path": "/server",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-thunderbolt",
                            "title": "服务监控",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        }
                    },
                    {
                        "id": 3600,
                        "parent_id": 3000,
                        "name": "system:onlineUser",
                        "component": "system/monitor/onlineUser/index",
                        "path": "/onlineUser",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-online",
                            "title": "在线用户",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        }
                    },
                    {
                        "id": 3700,
                        "parent_id": 3000,
                        "name": "system:cache",
                        "component": "system/monitor/cache/index",
                        "path": "/cache",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-dice",
                            "title": "缓存监控",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 3701,
                                "parent_id": 3700,
                                "name": "system:cache:monitor",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "获取Redis信息",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 3702,
                                "parent_id": 3700,
                                "name": "system:cache:delete",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "删除一个缓存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 3703,
                                "parent_id": 3700,
                                "name": "system:cache:clear",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "清空所有缓存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 3300,
                        "parent_id": 3000,
                        "name": "logs",
                        "component": "",
                        "path": "/logs",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-book",
                            "title": "日志监控",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 3850,
                                "parent_id": 3300,
                                "name": "system:queueLog",
                                "component": "system/logs/queueLog",
                                "path": "/queueLog",
                                "redirect": None,
                                "meta": {
                                    "type": "M",
                                    "icon": "icon-layers",
                                    "title": "队列日志",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                },
                                "children": [
                                    {
                                        "id": 3851,
                                        "parent_id": 3850,
                                        "name": "system:queueLog:delete",
                                        "component": "",
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": "",
                                            "title": "删除队列日志",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 3852,
                                        "parent_id": 3850,
                                        "name": "system:queueLog:updateStatus",
                                        "component": "",
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": "",
                                            "title": "更新队列状态",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    }
                                ]
                            },
                            {
                                "id": 3400,
                                "parent_id": 3300,
                                "name": "system:loginLog",
                                "component": "system/logs/loginLog",
                                "path": "/loginLog",
                                "redirect": None,
                                "meta": {
                                    "type": "M",
                                    "icon": "icon-idcard",
                                    "title": "登录日志",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                },
                                "children": [
                                    {
                                        "id": 3401,
                                        "parent_id": 3400,
                                        "name": "system:loginLog:delete",
                                        "component": "",
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": "",
                                            "title": "登录日志删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    }
                                ]
                            },
                            {
                                "id": 3500,
                                "parent_id": 3300,
                                "name": "system:operLog",
                                "component": "system/logs/operLog",
                                "path": "/operLog",
                                "redirect": None,
                                "meta": {
                                    "type": "M",
                                    "icon": "icon-robot",
                                    "title": "操作日志",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                },
                                "children": [
                                    {
                                        "id": 3601,
                                        "parent_id": 3500,
                                        "name": "system:onlineUser:index",
                                        "component": "",
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": "",
                                            "title": "在线用户列表",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 3602,
                                        "parent_id": 3500,
                                        "name": "system:onlineUser:kick",
                                        "component": "",
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": "",
                                            "title": "强退用户",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    },
                                    {
                                        "id": 3501,
                                        "parent_id": 3500,
                                        "name": "system:operLog:delete",
                                        "component": "",
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": "",
                                            "title": "操作日志删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    }
                                ]
                            },
                            {
                                "id": 3800,
                                "parent_id": 3300,
                                "name": "system:apiLog",
                                "component": "system/logs/apiLog",
                                "path": "/apiLog",
                                "redirect": None,
                                "meta": {
                                    "type": "M",
                                    "icon": "icon-calendar",
                                    "title": "接口日志",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                },
                                "children": [
                                    {
                                        "id": 3801,
                                        "parent_id": 3800,
                                        "name": "system:apiLog:delete",
                                        "component": "",
                                        "path": "/",
                                        "redirect": None,
                                        "meta": {
                                            "type": "B",
                                            "icon": "",
                                            "title": "接口日志删除",
                                            "hidden": True,
                                            "hiddenBreadcrumb": False
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "id": 4000,
                "parent_id": 0,
                "name": "devTools",
                "component": "",
                "path": "/devTools",
                "redirect": None,
                "meta": {
                    "type": "M",
                    "icon": "ma-icon-tool",
                    "title": "工具",
                    "hidden": False,
                    "hiddenBreadcrumb": False
                },
                "children": [
                    {
                        "id": 4100,
                        "parent_id": 4000,
                        "name": "setting:module",
                        "component": "setting/module/index",
                        "path": "/module",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-folder",
                            "title": "模块管理",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 4101,
                                "parent_id": 4100,
                                "name": "setting:module:save",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "新增模块",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4102,
                                "parent_id": 4100,
                                "name": "setting:module:delete",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "模块删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4103,
                                "parent_id": 4100,
                                "name": "setting:module:index",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "模块列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4104,
                                "parent_id": 4100,
                                "name": "setting:module:status",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "模块启停用",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4105,
                                "parent_id": 4100,
                                "name": "setting:module:install",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "安装模块",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 4200,
                        "parent_id": 4000,
                        "name": "setting:code",
                        "component": "setting/code/index",
                        "path": "/code",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "ma-icon-code",
                            "title": "代码生成器",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 4201,
                                "parent_id": 4200,
                                "name": "setting:code:preview",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "预览代码",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4202,
                                "parent_id": 4200,
                                "name": "setting:code:loadTable",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "装载数据表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4203,
                                "parent_id": 4200,
                                "name": "setting:code:delete",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "删除业务表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4204,
                                "parent_id": 4200,
                                "name": "setting:code:sync",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "同步业务表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4205,
                                "parent_id": 4200,
                                "name": "setting:code:generate",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "生成代码",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 4621,
                        "parent_id": 4000,
                        "name": "setting:datasource",
                        "component": "setting/datasource/index",
                        "path": "/setting/datasource",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-storage",
                            "title": "数据源管理",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 4622,
                                "parent_id": 4621,
                                "name": "setting:datasource:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据源管理列表",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4623,
                                "parent_id": 4621,
                                "name": "setting:datasource:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据源管理保存",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4624,
                                "parent_id": 4621,
                                "name": "setting:datasource:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据源管理更新",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4625,
                                "parent_id": 4621,
                                "name": "setting:datasource:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据源管理读取",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4626,
                                "parent_id": 4621,
                                "name": "setting:datasource:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据源管理删除",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4627,
                                "parent_id": 4621,
                                "name": "setting:datasource:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据源管理导入",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4628,
                                "parent_id": 4621,
                                "name": "setting:datasource:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "数据源管理导出",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 4400,
                        "parent_id": 4000,
                        "name": "setting:crontab",
                        "component": "setting/crontab/index",
                        "path": "/crontab",
                        "redirect": "",
                        "meta": {
                            "type": "M",
                            "icon": "icon-schedule",
                            "title": "定时任务",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 4401,
                                "parent_id": 4400,
                                "name": "setting:crontab:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "定时任务列表",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4402,
                                "parent_id": 4400,
                                "name": "setting:crontab:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "定时任务保存",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4403,
                                "parent_id": 4400,
                                "name": "setting:crontab:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "定时任务更新",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4404,
                                "parent_id": 4400,
                                "name": "setting:crontab:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "定时任务删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4405,
                                "parent_id": 4400,
                                "name": "setting:crontab:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "定时任务读取",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4406,
                                "parent_id": 4400,
                                "name": "setting:crontab:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "定时任务导入",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4407,
                                "parent_id": 4400,
                                "name": "setting:crontab:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "定时任务导出",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4408,
                                "parent_id": 4400,
                                "name": "setting:crontab:run",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "定时任务执行",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4409,
                                "parent_id": 4400,
                                "name": "setting:crontab:deleteLog",
                                "component": "",
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": "",
                                    "title": "定时任务日志删除",
                                    "hidden": True,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 4600,
                        "parent_id": 4000,
                        "name": "systemInterface",
                        "component": "setting/systemInterface/index",
                        "path": "/systemInterface",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-compass",
                            "title": "系统接口",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        }
                    }
                ]
            },
            {
                "id": 4601,
                "parent_id": 0,
                "name": "demo",
                "component": None,
                "path": "/demo",
                "redirect": None,
                "meta": {
                    "type": "M",
                    "icon": "IconTwitter",
                    "title": "演示区（可修改）",
                    "hidden": False,
                    "hiddenBreadcrumb": False
                },
                "children": [
                    {
                        "id": 4602,
                        "parent_id": 4601,
                        "name": "iframeDemo",
                        "component": None,
                        "path": "/",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "IconLaunch",
                            "title": "iFrame演示",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 4603,
                                "parent_id": 4602,
                                "name": "txy",
                                "component": None,
                                "path": "https://cloud.tencent.com/act/cps/redirect?redirect=1077&cps_key=1fd4777e14a33e75d9bfdb5e6a0ba0f2&from=console/",
                                "redirect": None,
                                "meta": {
                                    "type": "I",
                                    "icon": None,
                                    "title": "腾讯云",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4604,
                                "parent_id": 4602,
                                "name": "mineadminDoc",
                                "component": None,
                                "path": "https://doc.mineadmin.com",
                                "redirect": None,
                                "meta": {
                                    "type": "I",
                                    "icon": None,
                                    "title": "MineAdmin文档",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 4613,
                        "parent_id": 4601,
                        "name": "demo:qa",
                        "component": "demo/qa/index",
                        "path": "/demo/qa",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-home",
                            "title": "问答示例",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 4614,
                                "parent_id": 4613,
                                "name": "demo:qa:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "问答示例列表",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4615,
                                "parent_id": 4613,
                                "name": "demo:qa:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "问答示例保存",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4616,
                                "parent_id": 4613,
                                "name": "demo:qa:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "问答示例更新",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4617,
                                "parent_id": 4613,
                                "name": "demo:qa:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "问答示例读取",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4618,
                                "parent_id": 4613,
                                "name": "demo:qa:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "问答示例删除",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4619,
                                "parent_id": 4613,
                                "name": "demo:qa:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "问答示例导入",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4620,
                                "parent_id": 4613,
                                "name": "demo:qa:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "问答示例导出",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    },
                    {
                        "id": 4605,
                        "parent_id": 4601,
                        "name": "demo:example1",
                        "component": "demo/example1/index",
                        "path": "/demo/example1",
                        "redirect": None,
                        "meta": {
                            "type": "M",
                            "icon": "icon-home",
                            "title": "代码生成示例",
                            "hidden": False,
                            "hiddenBreadcrumb": False
                        },
                        "children": [
                            {
                                "id": 4608,
                                "parent_id": 4605,
                                "name": "demo:example1:update",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "代码生成示例更新",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4609,
                                "parent_id": 4605,
                                "name": "demo:example1:read",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "代码生成示例读取",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4610,
                                "parent_id": 4605,
                                "name": "demo:example1:delete",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "代码生成示例删除",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4611,
                                "parent_id": 4605,
                                "name": "demo:example1:import",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "代码生成示例导入",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4612,
                                "parent_id": 4605,
                                "name": "demo:example1:export",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "代码生成示例导出",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4606,
                                "parent_id": 4605,
                                "name": "demo:example1:index",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "代码生成示例列表",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            },
                            {
                                "id": 4607,
                                "parent_id": 4605,
                                "name": "demo:example1:save",
                                "component": None,
                                "path": "/",
                                "redirect": None,
                                "meta": {
                                    "type": "B",
                                    "icon": None,
                                    "title": "代码生成示例保存",
                                    "hidden": False,
                                    "hiddenBreadcrumb": False
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "id": 4500,
                "parent_id": 0,
                "name": "setting:config",
                "component": "setting/config/index",
                "path": "/system",
                "redirect": "",
                "meta": {
                    "type": "M",
                    "icon": "icon-settings",
                    "title": "系统设置",
                    "hidden": False,
                    "hiddenBreadcrumb": False
                },
                "children": [
                    {
                        "id": 4502,
                        "parent_id": 4500,
                        "name": "setting:config:index",
                        "component": "",
                        "path": "/",
                        "redirect": None,
                        "meta": {
                            "type": "B",
                            "icon": "",
                            "title": "配置列表",
                            "hidden": True,
                            "hiddenBreadcrumb": False
                        }
                    },
                    {
                        "id": 4504,
                        "parent_id": 4500,
                        "name": "setting:config:save",
                        "component": "",
                        "path": "/",
                        "redirect": None,
                        "meta": {
                            "type": "B",
                            "icon": "",
                            "title": "新增配置 ",
                            "hidden": True,
                            "hiddenBreadcrumb": False
                        }
                    },
                    {
                        "id": 4505,
                        "parent_id": 4500,
                        "name": "setting:config:update",
                        "component": "",
                        "path": "/",
                        "redirect": None,
                        "meta": {
                            "type": "B",
                            "icon": "",
                            "title": "更新配置",
                            "hidden": True,
                            "hiddenBreadcrumb": False
                        }
                    },
                    {
                        "id": 4506,
                        "parent_id": 4500,
                        "name": "setting:config:delete",
                        "component": "",
                        "path": "/",
                        "redirect": None,
                        "meta": {
                            "type": "B",
                            "icon": "",
                            "title": "删除配置",
                            "hidden": True,
                            "hiddenBreadcrumb": False
                        }
                    },
                    {
                        "id": 4507,
                        "parent_id": 4500,
                        "name": "setting:config:clearCache",
                        "component": "",
                        "path": "/",
                        "redirect": None,
                        "meta": {
                            "type": "B",
                            "icon": "",
                            "title": "清除配置缓存",
                            "hidden": True,
                            "hiddenBreadcrumb": False
                        }
                    }
                ]
            }
        ],
        "codes": [
            "*"
        ]
    }
}
