- 👋 Hi, I’m @palomaavena
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
palomaavena/palomaavena is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

let protoPaloma = {
    speak: function (line) {
        console.log(this.tipe + line);
    },
};
let student = Object.create(protoPaloma);
student.tipe = "Paloma";
student.speak("passionate about the ocean of data");

// → "Paloma passionate about the ocean of data!"
 
