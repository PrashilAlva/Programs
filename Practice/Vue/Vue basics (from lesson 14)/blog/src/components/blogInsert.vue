<template>
  <div>
    <h1>My BlogSpot</h1>
    <div v-if="!submitted"> 
      <h3 style="font-weight:lighter">Please Enter the Blog Below</h3>
      <div id="blogg">
        <form>
          <label>Blog Title:</label>
          <input type="text" placeholder="Blog Title" v-model.lazy="blog.title" required />
          <br />
          <br />
          <label>Blog Content:</label>
          <br />
          <br />
          <textarea
            placeholder="Content here..."
            style="width:300px;height:80px;"
            v-model.lazy="blog.content"
            required
          ></textarea>
        </form>
        <h3 style="font-weight:lighter">Choose the categories</h3>
        <label>Romantic</label>
        <input type="checkbox" value="Romantic" v-model="blog.categories" />
        <label>Horror</label>
        <input type="checkbox" value="Horror" v-model="blog.categories" />
        <label>Sci-fi</label>
        <input type="checkbox" value="Sci-fi" v-model="blog.categories" />
        <label>Travel</label>
        <input type="checkbox" value="Travel" v-model="blog.categories" />
        <br />
        <h3 style="font-weight=lighter">Author:</h3>
        <select v-model="blog.author">
          <option v-for="author in authors">{{author}}</option>
        </select>
        <br />
        <br />
        <button @click="post()">Submit</button>
      </div>
    </div>
    <p v-if="submitted">Your blog has been submitted successfully</p>
    <br />
    <br />
    <h2>Blog Preview</h2>
    <p><b>Blog Title</b>:{{blog.title}}</p>
    <p><b>Blog Content</b>:</p>
    <p>{{blog.content}}</p>
    <p><b>Blog Category</b>:</p>
    <ul>
      <li v-for="ele in blog.categories">{{ele}}</li>
    </ul>
    <p><b>Blog Author</b>:{{blog.author}}</p>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      blog: {
        title: "",
        content: "",
        categories: [],
        author: "",
      },
      submitted: false,
      authors: ["Seymour Lipschutz", "Prashil Alva", "William Shakespeare"]
    };
  },
  methods: {
    post: function() {
      this.$http
        .post("https://postblogs-83c5e.firebaseio.com/blogs.json", this.blog)
        .then(function(data) {
          this.submitted = !this.submitted;
          console.log(this.blog.categories)
        });
    }
  }
};
</script>

<style>
body {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#blogg {
  border: 2px ridge black;
  padding: 10px;
  border-radius: 2em;
  padding-left: 200px;
  padding-right: 200px;
}
</style>
