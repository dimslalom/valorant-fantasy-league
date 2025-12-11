import { useState, useEffect, use } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  // Fetch data when page loads
  useEffect(() => {
    // Fetch User ID 1 TEMPORARY
    axios.get('http://localhost:8000/users/1')
      .then(response => {
        setUser(response.data)
        setLoading(false)
      })
      .catch(error => {
        console.error('Error fetching user data:', error)
        setLoading(false)
      })
  }, [])

  if (loading) return <h1>Loading...</h1>
  if (!user) return <h1>Error loading user data</h1>

  return (
    <div className='container'>
      {/* Header Section */}
      <header>
        <h1>Valorant Fantasy League</h1>
        <div className='user-info'>
          <p>Manager: <strong>{user.username}</strong></p>
          <p>Credits: <span className='credits'>{user.credits}</span></p>
        </div>
      </header>

      {/* Cards Display Section */}
      <main>
        <h2>Your Roster</h2>
        <div className='cards-grid'>
          {user.cards.map(card => (
            <div key={card.id} className='card'>
              <div className='card-header'>
                <span className='role'>{card.player_role}</span>
            </div>

            <div className='card-image'>
              {/* Placeholder for player image */}
              <h3>{card.player_name}</h3>
            </div>

            <div className='card-details'>
              <p className='team'>{card.team_name}</p>
              <div className='stats'>
                <span>MEC: {card.mechanics}</span>
                <span>SEN: {card.game_sense}</span>
                <span>CON: {card.consistency}</span>
                <span>CLU: {card.clutch_factor}</span>
                <span>LEA: {card.leadership}</span>
              </div>
            </div>
          </div>
          ))}
        </div>
      </main>
    </div>
  )
}

export default App