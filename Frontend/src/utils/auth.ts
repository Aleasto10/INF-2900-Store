export function getCurrentUser() {
  const user = localStorage.getItem("account")
  return user ? JSON.parse(user) : null
}