import viewBlog from './components/blogView.vue'
import addBlog from './components/blogInsert.vue'
import singleBlog from './components/singleBlog.vue'

export default[
    {path:'/',component:viewBlog},
    {path:'/add',component:addBlog},
    {path:'/blog/:id',component:singleBlog}
]